# -*- coding: utf-8 -*-

import threading
from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):
  def __init__(self, data: Optional[T] = None):
    self.data = data
    self.next = None
    
  
class ConSet(Generic[T]):
  def __init__(self):
    self.head = Node[T]()
    self.tail = Node[T]()
    self.ConSetLock = threading.Lock()
    self.cv = threading.Condition(self.ConSetLock)
    

  def add(self, item: T):
    temp = Node[T](item)
    self.ConSetLock.acquire()
    if self.tail.data == None:
        self.head = self.tail = temp
        self.cv.notify()
        self.ConSetLock.release()
        return
    self.tail.next = temp
    self.tail = temp
    self.cv.notify()
    self.ConSetLock.release()
  

  def remove(self):
    self.ConSetLock.acquire()
    while self.head.data == None:
      self.cv.wait()
    temp = self.head
    val = temp.data
    if temp.next == None:
      self.head = Node()
    else:
      self.head = temp.next
    if self.head.data == None:
      self.tail = Node()
    self.ConSetLock.release()
    return val 
