# List and Linked List backed Queues are both included in this module for comparison

from typing import TypeVar, Generic, Optional

from linked_lists.singly_linked_list import SinglyLinkedList


T = TypeVar('T')


class ListQueue(Generic[T]):
    '''
    A FIFO queue implement on a Python list. This structure enqueues on 
    the right and dequeues on the left. 

    Python's list.append operates at O(1) time, this queue inherits the same
    and runs in O(1) time for insertion operations. Deletion requires O(n)
    time to shift left each list element. 

    This implementation chooses O(1) enqueue and O(n) dequeue. 
    The alternative — inserting at index 0 — would invert these costs.

    '''


    def __init__(self) -> None:
        self._data: list[T] = []


    def __repr__(self):
        return f"Queue({self._data!r})"


    def __str__(self):
        '''
        Reversed string to the more logical display order.
        '''
        items = [repr(v) for v in self._data]
        return f"Front -> {' -> '.join(items)}"


    def __len__(self):
        return len(self._data)


    def enqueue(self, item: T) -> None:
        self._data.append(item)


    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("queue is empty")

        dequeued: T = self._data[0]
        self._data = self._data[1:]
        return dequeued 


    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("queue is empty")

        return self._data[0]


    def is_empty(self) -> bool:
        return len(self._data) == 0


class LinkedListQueue(Generic[T]):
    '''
    A FIFO queue implemented on a singly linked list. This structure enqueues on 
    the right and dequeues on the left. 
    
    The underlying Singly Linked List maintains both head and tail pointers; therefore, 
    this representation of a Queue operates at O(1) time complexity for both insertion 
    and deletion operations.
    '''
    def __init__(self) -> None:
        self._data: SinglyLinkedList[T] = SinglyLinkedList()


    def __repr__(self):
        items = [repr(v) for v in self._data.to_list()]
        return f"Queue([{', '.join(items)}])"


    def __str__(self):
        items = [repr(v) for v in self._data.to_list()]
        return f"Front -> {' -> '.join(items)}"


    def __len__(self):
        return len(self._data)


    def enqueue(self, item: T) -> None:
        self._data.append_fast(item)


    def dequeue(self) -> T:
        '''
        Implementing a LinkedListStack.delete_head() would be best.
        This method relies on SinglyLinkedList.delete() which is intended to 
        delete the first occurance of an index, not simply the head.
        '''
        if self.is_empty():
            raise IndexError('Queue is empty')

        front: T = self.peek()
        self._data.delete(front)
        return front


    def peek(self) -> T:
        if self.is_empty():
            raise IndexError('Queue is empty')

        assert self._data.head != None      # This is to make MyPy happy

        return self._data.head.value


    def is_empty(self) -> bool:
        return len(self._data) == 0


if __name__ == "__main__":
    # list backed queue debug
    print('ListQueue')
    lq: ListQueue = ListQueue()
    for v in range(5):
        lq.enqueue(v)
    print(lq)
    print(repr(lq))
    removed = lq.dequeue()
    print(f'removed: {removed}')
    print(lq)

    print('-----')

    # linked list backed queue debug
    print('LinkedListQueue')
    llq: LinkedListQueue[int] = LinkedListQueue()
    for x in range(0, 50, 10):
        llq.enqueue(x)
    print(llq)
    print(repr(llq))
    removed = llq.dequeue()
    print(f'removed: {removed}')
    print(llq)
