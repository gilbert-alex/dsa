from typing import Any, Optional
from collections.abc import Iterator


class Node():
    def __init__(self, value):
        self.value = value


class HashSet():
    ''' 
    A hash set implemented with linear probing to handle collisions.

    Internally maintains a Python list of Nodes.
    Automatically resizes when the load factor exceeds CAPACITY.

    Time complexity (average / worst):
        get: O(1) / O(n)
        set: O(1) amortized / O(n)
        delete: O(1) / O(n)

    Space complexity: 
        O(n)
    '''

    DEFAULT_CAPACITY = 8
    MAX_LOAD = .75
    _TOMBSTONE = object()
    

    def __init__(self, capacity: int = DEFAULT_CAPACITY) -> None:
        self._capacity: int = capacity
        self._count: int = 0
        self._buckets: list[Node | None] = [None] * self._capacity


    def __str__(self) -> str:
        pairs = {
                index: node.value
                for index, node in enumerate(self._buckets)
                if node is not None 
                if node is not self._TOMBSTONE
                }

        return str(pairs)


    def __repr__(self):
        return (
                f"capacity  : {self._capacity}\n"
                f"count     : {self._count}\n"
                f"load      : {self._count / self._capacity:.2f}\n"
                )


    def __len__(self):
        return self._count


    def set(self, value: Any) -> None:
        # +1 count considers the current value being added
        if self._is_resize_required(self._count + 1, self._capacity):
            self._resize()

        self._insert(value)


    def get(self, target: Any) -> Any:
        index = self._scan_for_target(target)

        if index is None:
            raise ValueError(f'{target} not found')
        else:
            return self._buckets[index].value


    def delete(self, target: Any) -> Any:
        index = self._scan_for_target(target)
        if index is None:
            raise ValueError(f'{target} not found')
        else:
            self._buckets[index] = self._TOMBSTONE
            self._count -= 1


    def _hash(self, value: str) -> int:
        ''' Intentionally simple for now. 
            Include a prime multiplication factor to improve distribution.
        '''
        buffer = 0
        chars = list(value)

        for char in chars:
            buffer = (buffer + ord(char.lower())) % self._capacity
        return buffer


    def _probe(self, start: int) -> Iterator[int]:
        ''' Generator function starting at start and wraps once.
        '''
        index: int = start
        yield index
        index = self._get_next_index(index)
        while index != start:
            yield index
            index = self._get_next_index(index)


    def _get_next_index(self, index: int) -> int:
        ''' Increment index with wrap.
        '''
        return (index + 1) % self._capacity


    def _find_empty_bucket(self, start: int) -> int:
        for index in self._probe(start):
            bucket = self._buckets[index]
            if bucket == None or bucket is self._TOMBSTONE:
                return index

        raise ValueError('All buckets are full')


    def _scan_for_target(self, target: Any) -> Optional[int]:
        start = self._hash(str(target))

        for index in self._probe(start):
            bucket = self._buckets[index]
            if bucket is None:
                return None
            if bucket == self._TOMBSTONE:
                continue
            if bucket.value == target:
                return index

        return None


    def _insert(self, value: Any) -> None:
        node = Node(value)
        index = self._hash(str(value))
        existing_value = self._buckets[index]

        if existing_value is None or existing_value is self._TOMBSTONE:
            self._buckets[index] = node
        else:
            self._buckets[self._find_empty_bucket(index)] = node

        # Incrementing this variable here because _resize calls this function
        self._count += 1


    def _is_resize_required(self, count: int, capacity: int) -> bool:
        load_factor: float = count / capacity
        return True if load_factor >= HashSet.MAX_LOAD else False


    def _resize(self) -> None:
        old_buckets = self._buckets
        new_capacity = self._capacity * 2
        self._buckets = [None] * new_capacity
        self._capacity = new_capacity
        self._count = 0

        for b in old_buckets:
            if isinstance(b, Node):
                self._insert(b.value)


if __name__ == "__main__":
    pass
