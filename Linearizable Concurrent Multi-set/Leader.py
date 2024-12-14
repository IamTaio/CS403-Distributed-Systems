from threading import *
import random
from ConSet import *

n = 4
b = Barrier(n)
mailboxes = []
for i in range(n):
    s = ConSet[tuple]()
    mailboxes.append(s)

printlock = threading.Lock()

def nodeWork(id, num):
    leader = -1
    round = 1
    max_prop = num * num
    while leader == -1:
        proposal = random.randint(0, max_prop)
        message = (proposal, id)
        printlock.acquire()
        print("Node " + str(id) + " proposes value " + str(proposal) + " for round " + str(round)  + ".")
        printlock.release()
        for i in range(num):
            mailboxes[i].add(message)
        count = 0 
        max = (-1, 0)
        while count < num:
            element = mailboxes[id].remove()
            count = count + 1
            if element[0] == max[0]:
                value = max[0]
                max = (value, -1)
            elif element[0] > max[0]:
                max = element
        round = round + 1
        if max[1] != -1:
            leader = max
            printlock.acquire()            
            print("Node " + str(id) + " decided " + str(max[1]) + " as leader." )
            printlock.release()
        else:
            printlock.acquire()
            print("Node" + str(id) + " could not decide on the leader and moves to the round " + str(round) + ".")
            printlock.release()
        b.wait()
threadlist = []

for i in range(len(mailboxes)):
    thread = threading.Thread(target=nodeWork, args=(i, n))
    threadlist.append(thread)

for i in range(len(mailboxes)):
    threadlist[i].start()

for i in range(len(mailboxes)):
    threadlist[i].join()




