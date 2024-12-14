from abc import ABC, abstractmethod
import zmq
import os
import json
import time
from math import ceil, floor
from multiprocessing import Process

class MapReduce(ABC):
    def __init__(self, numworkers):
        self.numworkers = numworkers
    
    def __producer__(self, dataset):
        numWorkers = self.numworkers
        numrecords = len(dataset)
        context = zmq.Context()
        socket = context.socket(zmq.PUSH)
        socket.bind("tcp://127.0.0.1:5557")
        div = ceil(numrecords/numWorkers)
        k = 0
        j = 0
        #remRecords = 0
        div = floor(numrecords/numWorkers)
        remainder = numrecords % numWorkers
        thislist = []
        for i in range(numWorkers):
            thislist.append(div)
        i = 0
        while (remainder > 0):
            thislist[i] = thislist[i] + 1
            i = i + 1
            remainder = remainder - 1
        for m in range(numWorkers):
            j += thislist[m]
            subset = dataset[k:j]
            socket.send_json(subset)
            k += thislist[m]
            time.sleep(1)
            

    def __consumer__(self):
        print ('Consumer PID:', os.getpid())
        context = zmq.Context()
        receiver = context.socket(zmq.PULL)
        receiver.connect("tcp://127.0.0.1:5557")
        partial = receiver.recv_json()
        #partial = json.loads(partial)
        result = self.Map(partial)
        sender = context.socket(zmq.PUSH)
        sender.connect("tcp://127.0.0.1:5558")
        sender.send_json(result)
        return

    def __result_collector__(self):
        numWorkers = self.numworkers
        print ('ResultCollector PID:', os.getpid())
        context = zmq.Context()
        results_receiver = context.socket(zmq.PULL)
        results_receiver.bind("tcp://127.0.0.1:5558")
        collecter_data = []
        for x in range(numWorkers):
            result = results_receiver.recv_json()
            collecter_data.append(result)
        final = self.Reduce(collecter_data)
        f = open("results.txt", "w")
        f.write(str(final))
        f.close()

    def start(self, filename):
        f = open(filename, "r")
        numWorkers  = self.numworkers
        listitems = []
        for line in f:
            line = line.strip('\n')
            line = line.split('\t')
            for i in range(len(line)):
                line[i] = int(line[i])
            listitems.append(line)
        Collector = Process(target=self.__result_collector__)
        consumers = []
        for x in range(numWorkers):
            consumer = Process(target=self.__consumer__)
            consumers.append(consumer)
        Producer = Process(target=self.__producer__, args=(listitems,))
        Collector.start()
        for i in range(numWorkers):
            consumers[i].start()
        Producer.start()
        Producer.join()
        for i in range(numWorkers):
            consumers[i].join()
        Collector.join()

    @abstractmethod    
    def Map(self, parts):
        pass

    @abstractmethod
    def Reduce(self, dicts):
        pass
