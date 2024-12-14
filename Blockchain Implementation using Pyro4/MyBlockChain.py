from __future__ import annotations
import threading
import Pyro4
from Pyro4 import naming

@Pyro4.expose
class MyBlock:
    def __init__(self, transaction = ()):
        self.transaction = transaction
        self.next = None

    def transactionType(self):
        if len(self.transaction) == 0:
            return None
        return self.transaction[0]    

    def arguments(self):
        if len(self.transaction) == 0:
            return None
        return self.transaction[1]


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class MyBlockChain:
    def __init__(self, name):
        self.head = None
        self.chainName = name
        self.lock = threading.Lock()
        with Pyro4.Daemon() as Daemon:
            self.uri = Daemon.register(self)
            with Pyro4.locateNS() as ns:
                ns.register(name, self.uri)
            Daemon.requestLoop()


    def createAccount(self, amount):
        if self.head == None:
            self.head = MyBlock(transaction = ("CREATEACCOUNT",(1, amount)))
            accNo = 1
        else:
            max = 0
            temp = self.head
            while temp.next != None and temp.transactionType() != 'CREATEACCOUNT':
                temp = temp.next
            args = temp.arguments()
            if temp.transactionType() != 'CREATEACCOUNT':
                for i in range(2):
                    if args[i] > max:
                        max = args[i]
            else:
                args = temp.arguments()
                if args[0] > max:
                    max = args[0]
            accNo = max+1
            block = MyBlock(transaction = ("CREATEACCOUNT",(max+1, amount)))
            block.next = self.head
            self.head = block
        return accNo
    
    def transfer(self, accfrom, to, amount):
        self.lock.acquire()
        if not self.accExists(accfrom):
            self.lock.release()
            return -1
        if not self.accExists(to):
            self.lock.release()
            return -1
        FromBalance = self.calculateBalance(accfrom)
        ToBalance = self.calculateBalance(to)
        if (FromBalance - amount) < 0:
            self.lock.release()
            return -1
        if (ToBalance + amount) < 0:
            self.lock.release()
            return -1
        block = MyBlock(transaction = ("TRANSFER", (accfrom, to, amount)))
        block.next = self.head
        self.head = block
        self.lock.release()
        return 1
    
    def exchange(self, accFrom, to, toChain, amount):
        if not self.accExists(accFrom):
            return -1
        if not toChain.accExists(to):
            return -1
        if amount > 0: 
            self.lock.acquire()
            FromBalance = self.calculateBalance(accFrom)
            if (FromBalance - amount) < 0:
                self.lock.release()
                return -1
        elif amount < 0:
           return  toChain.exchange(accFrom, to, self, (amount * -1))
        toName = toChain.name()
        fromBlock = MyBlock(transaction = ("EXCHANGE", (accFrom, to, str(toName), amount)))
        toChain.insertTx("EXCHANGE", (accFrom, to, self.name(), amount))
        fromBlock.next = self.head
        self.head = fromBlock
        self.lock.release()
        return 1
            
    def name(self):
        return self.chainName

    def calculateBalance(self, accId):
        balance = 0
        temp = self.head
        if not self.accExists(accId):
            return -1
        while temp != None:
            args = temp.arguments()
            if temp.transactionType() == "CREATEACCOUNT":
                if args[0] == accId:
                    balance += args[1]
            elif temp.transactionType() == "TRANSFER":
                if args[0] == accId:
                    balance -= args[2]
                if args[1] == accId:
                    balance += args[2]
            elif temp.transactionType() == "EXCHANGE":
                if args[0] == accId:
                    balance -= args[3]
                elif args[1] == accId:
                    balance += args[3]
            temp = temp.next
        return balance
    
    def insertTx(self, call, arguments):
        block = MyBlock(transaction= (call, arguments))
        block.next = self.head
        self.head = block

    def transactionExists(self, call, arguments):
        if self.head == None:
            return False
        temp = self.head

    def accExists(self, accId):
        if self.head == None:
            print("No accounts created yet")
            return False
        temp = self.head
        while temp != None:
            args = temp.arguments()
            if temp.transactionType() == "CREATEACCOUNT":
                if accId == args[0]:
                    return True
            temp = temp.next
        return False
    
    def printChain(self):
        if self.head == None:
            print("No accounts created yet")
            return False
        temp = self.head
        transactions = []
        while temp != None:
            transactions.append(temp)
            temp = temp.next
        transactions.reverse()
        for i in transactions:
            args = i.arguments()
            transaction = i.transactionType()
            print(transaction,args)


                

