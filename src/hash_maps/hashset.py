from typing import Any


class Node():
    def __init__(self, value):
        self.value = value


class HashSet():
    ''' 
    A hash set implemented with linear probing to handle collisions.

    Interanlly maintains a Python list of Nodes.
    Automatically resizes when the load factor exceeds CAPACITY.

    Attributes:
        DEFAULT_CAPACITY (int): Initial number of buckets.
        MAX_LOAD (float): Threshold to trigger resize (len / capacity)

    Time complexity (average / worst):
        get: O(1) / O(n)
        set: O(1) amortized / O(n)
        delete: O(1) / O(n)

    Space complexity: 
        O(n)
    '''

    DEFAULT_CAPACITY = 8
    CAPACITY = .75
    

    def __init__(self, capacity: int = DEFAULT_CAPACITY) -> None:
        self._capacity = capacity
        self._len = 0
        self._buckets: list[Node | None] = [None] * self._capacity


    def set(self, value: Any) -> None:
        node = Node(value)
        index = self._hash(str(value))
        value = self._buckets[index]

        if value is None:
            self._buckets[index] = node
        else:
            self._buckets[self._find_empty_bucket(index)] = node


    def get(self, value: Any) -> Any:
        pass


    def delete(self, value: Any) -> Any:
        pass


    def _hash(self, value: str) -> int:
        buffer = 0
        chars = list(value)

        for char in chars:
            buffer = (buffer + ord(char.lower())) % self._capacity
        return buffer


    def _find_empty_bucket(self, index: int) -> int:
        '''
        Called on a collision to lineraly probe each bucket for the next
        empty bucket.
        '''
        start = index
        next = self._get_next_index(start)

        while next != start:
            if self._buckets[next] is None:
                return next
            next = self._get_next_index(next)

        raise ValueError('All buckets are full')


    def _get_next_index(self, index):
        ''' Increment index with wrap '''
        return (index + 1) % self._capacity

    def _resize(self) -> None:
        pass
