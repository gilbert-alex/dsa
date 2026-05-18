# List and Linked List backed Stacks are both included in this module for comparison

from typing import Any

from linked_lists.singly_linked_list import SinglyLinkedList


class ListStack:
    '''
    A LIFO stack implemented on a Python list. This structure operates on 
    the n-th index of the list where n is the length - 1.
    Assuming the Python list itself operates at O(1) time, this representation 
    of a stack also operates at O(1) time complexity for both insertion 
    and deletion operations.
    '''

    def __init__(self) -> None:
        self._data: list = []


    def __repr__(self):
        return f"Stack({self._data})"


    def __str__(self):
        parts = self._data
        parts.reverse()
        return f"Top -> {parts}"


    def __len__(self):
        return len(self._data)


    def push(self, item: Any) -> None:
        self._data.append(item)


    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._data.pop()


    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._data[-1]


    def is_empty(self) -> bool:
        return len(self._data) == 0


class LinkedListStack:
    '''
    A LIFO stack implemented on a singly linked list. This structure operates on 
    the n-th index of the list where n is the length - 1.
    This representation of a stack operates at O(1) time complexity for both 
    insertion and deletion operations.
    '''
    def __init__(self):
        self._data = SinglyLinkedList()


    def __repr__(self):
        pass


    def __str__(self):
        parts = [str(v) for v in self._data.to_list()]
        parts.append('None')
        return f'Parts= {" -> ".join(parts)}'


    def __len__(self):
        return self._data.__len__()


    def push(self, value):
        self._data.prepend(value)
        

    def pop(self):
        top = self.peek()
        self._data.delete(top)
        return(last)


    def peek(self):
        if not self._data.head.value:
            raise IndexError('Stack is empty')

        return self._data.tail.value

if __name__ == "__main__":

    print('---')
    ls = ListStack()
    for v in [50, 60, 70]:
        ls.push(v)
    print(repr(ls))
    print(ls)

    lls = LinkedListStack()
    for v in [10, 20, 30]:
        lls.push(v)
    print(lls)
