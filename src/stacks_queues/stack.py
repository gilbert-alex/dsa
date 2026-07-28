from typing import TypeVar, Generic, cast

from linked_lists.singly_linked_list import SinglyLinkedList

T = TypeVar('T')

class ListStack(Generic[T]):
    '''
    A LIFO stack implemented on a Python list. This structure operates on 
    the n-th index of the list where n is the length - 1. 
    
    By operating on the n-th index side, the Python's list.append and 
    list.pop both operates at O(1) time, this stack inherits the same and 
    runs in O(1) time for both insertion and deletion operations.

    The __str__ method reverses the native ordering of the Python list to 
    show a more intuitive string representation of a stack.
    '''

    def __init__(self) -> None:
        self._data: list[T] = []


    def __repr__(self) -> str:
        '''
        As this implementation appends new items on the right side of the 
        Python list, this string similarly displays the top of the stack 
        on the right side.
        '''
        #"!r" is the equivalent of "repr(d) for d in self._data"
        return f"Stack({self._data!r})"


    def __str__(self) -> str:
        '''
        Reversed string to the more logical display order.
        '''
        items = [repr(v) for v in reversed(self._data)]
        return f"Top -> {' -> '.join(items)}"


    def __len__(self) -> int:
        return len(self._data)


    def push(self, item: T) -> None:
        self._data.append(item)


    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("stack is empty")

        return self._data.pop()


    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("stack is empty")

        return self._data[-1]


    def is_empty(self) -> bool:
        return len(self._data) == 0


class LinkedListStack(Generic[T]):
    '''
    A LIFO stack implemented on a singly linked list. This structure operates on 
    the 0-th index of the list.

    This representation of a stack operates at O(1) time complexity for both 
    insertion and deletion operations.
    '''
    def __init__(self) -> None:
        self._data = SinglyLinkedList()


    def __repr__(self) -> str:
        '''
        The base linked list builds with a prepend method such that the 
        top of the Stack is always at the Linked List head.
        '''
        items = [repr(v) for v in self._data.to_list()]
        return f"Stack([{', '.join(items)}])"


    def __str__(self) -> str:
        items = [repr(v) for v in self._data.to_list()]
        return f"Top -> {' -> '.join(items)}"


    def __len__(self) -> int:
        return len(self._data)


    def push(self, item: T) -> None:
        self._data.prepend(item)
        

    def pop(self) -> T:
        '''
        Implementing a LinkedListStack.delete_head() would be best.
        This method relies on SinglyLinkedList.delete() which is intended to 
        delete the first occurance of an index, not simply the head.
        '''
        if self.is_empty():
            raise IndexError('Stack is empty')

        top: T = self.peek()
        self._data.delete(top)
        return(top)


    def peek(self) -> T:
        if self.is_empty():
            raise IndexError('Stack is empty')

        head = self._data.head
        assert head is not None
        return head.value


    def is_empty(self) -> bool:
        return True if self._data.head is None else False


if __name__ == "__main__":
    # list backed stack debug
    print('ListStack:')
    ls: ListStack[object] = ListStack()
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
    lls: LinkedListStack[object] = LinkedListStack()
    for v in [10, 20, 30, '40', 'fifty', '', 100]:
        lls.push(v)
    print(lls)
    print(repr(lls))
    popped = lls.pop()
    print(f'removed: {popped}')
    print(lls)
