class Stack:
    '''
    Implements a LIFO array which pushes and pops from the nth index
    where n is the length of the array -1.
    This representation of a Stack operates at a time complexity of 
    O(1) for both insertion and deletion operations.
    '''

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"
