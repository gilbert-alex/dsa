# List and Linked List backed Queues are both included in this module for comparison

from typing import Any

from linked_lists.singly_linked_list import SinglyLinkedList


class ListQueue:
    '''
    A FIFO queue implement on a Python list. This structure enqueues on 
    the right and dequeues on the left. 
    The __str__ method reverses the native ordering of the Python list to
    show a more intuitive string representation of a stack.
    Assuming the Python list itself operates at O(1) time, this representation
    of a queue also operates at O(1) time complexity for insertion. Deletion
    requires O(n) time complexity to shift the index of each list element. The
    only optimization when using a List as data store is to choose when to 
    reindex elements; on insertion or deletion. 
    '''


    def __init__(self) -> None:
        self._data = []


    def __repr__(self):
        return f"Queue({self._data!r})"


    def __str__(self):
        '''
        Reversed string to the more logical display order.
        '''
        parts = [repr(v) for v in reversed(self._data)]
        return f"Front -> {' -> '.join(parts)}"


    def __len__(self):
        return len(self._data)


    def enqueue(self, item: Any) -> None:
        self._data.append(item)


    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("queue is empty")

        dequeued = self._data[0]
        self._data = self._data[1::]
        return dequeued 


    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("queue is empty")

        return self._data[0]


    def is_empty(self) -> bool:
        return len(self._data) == 0





if __name__ == "__main__":
    print('ListQueue')
    lq = ListQueue()
    for v in range(3):
        lq.enqueue(v)
    print(lq)
    print(repr(lq))
