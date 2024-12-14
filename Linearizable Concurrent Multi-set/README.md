# Programming Assignment 1 Report

## Goal

To design an implementation of a Linearizable Concurrent Multi-Set and to use this implementation to simulate a leader election function distributed across multiple nodes.

## The Interface of the Concurrent Multi-Set

```java
interface Set {
    None add(Element x);
    Element remove();
}
```

## Expected Behavior

* Add method should always add a new element x to the set
* While there are elements in the set, the remove method should return an element contained within the set and remove that element from the set
* If there are no elements in the set, then the remove method should block and wait for an element to be added to the set

## Invariants

* Multiple elements with the exact same value can exist within the set at a time

## Implementation of Concurrent MultiSet

The ConSet implementation is built using a linked list with queue-like insertions and deletions, and a coarse-grained synchronization scheme. The coarse-grained synchronization is used because, as noted by Herlihy and Shavit in The Art of Multiprocessor Programming, it has the main advantage of being obviously correct.

However, it is also inefficient when there is high contention, as it enforces a sequential bottleneck. To address this inefficiency, we utilize queue-like insertions and deletions, adding new nodes to the end of the list and removing them from the front. This makes the add and remove methods O(1), thereby reducing the performance cost of using coarse-grained synchronization.

## Algorithm

### Constructor
```python
Class ConSet():
    Head = Tail = None
    ConSetLock = New Lock()
    ConSetConditionalLock = New ConditionalLock(ConSetLock)
```

### Insertion
```python
Add(Element X):
    Node = new node(Element(X))
    AcquireConSetLock
    If set is empty {
        Head = tail = Node
        Signal ConSetConditionalLock
        Release ConSetLock
        Return
    }
    Else {
        Tail.next = Node
        Tail = Node
    }
    ConSetConditionalLock
    Release ConSetLock
    Return
```

### Deletion
```python
Remove():
    Acquire ConSetLock
    If set is empty {
        ConSetConditionalLock.Wait()
    }
    Temp = Head
    Value = Temp.Element
    If Temp.next = None {
        Head = Tail = None
    }
    Else {
        Head = Head.Next
    }
    Release ConSetLock
    Return Value
```

## Linearizability Analysis

The implementation is linearizable, as demonstrated by identifying the linearization points of each method:

### Add Method
The linearization point can be either:
* The moment when the lock is acquired
* The point where Tail is set to the new Node (guaranteed to happen on every call due to locks)

### Remove Method
Linearization points are:
* When the locks are acquired
* For a set with one element: the point where head is set to none
* For multiple elements: when Head is set to its next element

## Implementation of Leader Method

To guarantee that the leader is only picked from the correct election round:

* Messages are tuples of the form `<number, id>`
* The barrier function from the Python threading library ensures all messages have completely cleared their set before new nodes are added
* Conditional locks ensure the remove method releases the lock while waiting for new elements, improving efficiency

## Synchronization Details

While coarse-grained synchronization provides obvious correctness, we enhance it with conditional locks so that:
* The remove method does not hold the lock while waiting for elements
* The method releases the lock and sleeps until an element is added
* A signal is sent for elements added to both empty and non-empty sets

This implementation balances correctness with performance, providing thread-safe operations while minimizing contention through efficient queue-like operations and proper lock management.
