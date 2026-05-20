# List and Linked List backed Stacks are both included in this module for comparison

from typing import Any

from linked_lists.singly_linked_list import SinglyLinkedList


class ListStack:
    '''
    A LIFO stack implemented on a Python list. This structure operates on 
    the n-th index of the list where n is the length - 1. The methods __str__ and
    __repr__ reverse the native implementation of the Python list to be a more
    intuitive string representation of a stack.
    Assuming the Python list itself operates at O(1) time, this representation 
    of a stack also operates at O(1) time complexity for both insertion 
    and deletion operations.
    '''

    def __init__(self) -> None:
        self._data: list = []


    def __repr__(self):
        '''
        As this implementation appends new items on the right side of the 
        Python list, this string similarly displays the top of the stack 
        on the right side.
        '''
        #"!r" is the equavalent of "repr(d) for d in self._data"
        return f"Stack({self._data!r})"


    def __str__(self):
        '''
        Reversed string to the more logical display order.
        '''
        parts = [repr(v) for v in reversed(self._data)]
        return f"Top -> {' -> '.join(parts)}"


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
    the 0-th index of the list.
    This representation of a stack operates at O(1) time complexity for both 
    insertion and deletion operations.
    '''
    def __init__(self):
        self._data = SinglyLinkedList()


    def __repr__(self):
        '''
        The base linked list builds with a prepend method such that the 
        top of the Stack is always at the Linked List head.
        '''
        parts = [repr(v) for v in self._data.to_list()]
        return f"Stack([{', '.join(parts)}])"


    def __str__(self):
        parts = [repr(v) for v in self._data.to_list()]
        return f"top -> {' -> '.join(parts)}"


    def __len__(self):
        return len(self._data)


    def push(self, value):
        self._data.prepend(value)
        

    def pop(self):
        '''
        It's probably cleaner to create a "delete_head" method on the linked list
        instead of relying on this peek and pop combo.
        I dont have to worry about popping a value not in the list because
        the popped value is not from user input.
        '''
        if self.is_empty():
            raise IndexError('Stack is empty')

        top = self.peek()
        self._data.delete(top)
        return(top)


    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')

        return self._data.head.value


    def is_empty(self) -> bool:
        return True if self._data.head is None else False


if __name__ == "__main__":
    # list backed stack debug
    print('ListStack:')
    ls = ListStack()
    for v in [1, 2, 3, '4', 'five', '', 10]:
        ls.push(v)
    print(ls)
    print(repr(ls))
    removed = ls.pop()
    print(f'removed: {removed}')
    print(ls)

    print('---')
    # linked list backed stack debug
    print('LinkedListStack:')
    lls = LinkedListStack()
    for v in [10, 20, 30, '40', 'fifty', '', 100]:
        lls.push(v)
    print(lls)
    print(repr(lls))
    popped = lls.pop()
    print(f'removed: {popped}')
    print(lls)
