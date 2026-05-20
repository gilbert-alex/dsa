# List and Linked List backed Queues are both included in this module for comparison

from typing import Any

from linked_lists.singly_linked_list import SinglyLinkedList


class ListQueue:
    '''
    A FIFO queue implement on a Python list. This structure enqueues on 
    the right and dequeues on the left. 
    The __str__ method reverses the native ordering of the Python list to
    show a more intuitive string representation of a queue.
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
        items = [repr(v) for v in self._data]
        return f"Front -> {' -> '.join(items)}"


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


class LinkedListQueue:
    '''
    A FIFO queue implemented on a singly linked list. This structure enqueues on 
    the right and dequeues on the left. This design is necessary because the 
    underlying Linked List is only capable of deleting the first from left, or all, 
    occurances of a target item's value. 
    The underlying Linked List maintains a previous node reference pointer; therefore, 
    this representation of a queue operates at O(1) time complexity for both insertion 
    and deletion operations.
    '''
    def __init__(self) -> None:
        self._data = SinglyLinkedList()


    def __repr__(self):
        items = [repr(v) for v in self._data.to_list()]
        return f"Stack([{', '.join(items)}])"


    def __str__(self):
        items = [repr(v) for v in self._data.to_list()]
        return f"top -> {' -> '.join(items)}"


    def __len__(self):
        return len(self._data)


    def enqueue(self, item: Any) -> None:
        self._data.append_fast(item)


    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError('Queue is empty')

        front = self.peek()
        self._data.delete(front)
        return front


    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError('Queue is empty')

        return self._data.head.value


    def is_empty(self) -> bool:
        return len(self._data) == 0


if __name__ == "__main__":
    # list backed queue debug
    print('ListQueue')
    lq = ListQueue()
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
    llq = LinkedListQueue()
    for x in range(0, 50, 10):
        llq.enqueue(x)
    print(llq)
    print(repr(llq))
    removed = llq.dequeue()
    print(f'removed: {removed}')
    print(llq)
