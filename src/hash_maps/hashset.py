from typing import Any


class Node():
    def __init__(self, value):
        self.value = value


class HashSet():
    ''' 
    A hash set implemented with linear probing to handle collisions.

    Interanally maintains a Python list of Nodes.
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
    MAX_LOAD = .75
    

    def __init__(self, capacity: int = DEFAULT_CAPACITY) -> None:
        self._capacity = capacity
        self._count = 0
        self._buckets: list[Node | None] = [None] * self._capacity


    def __str__(self) -> str:
        load_factor = self._count / self._capacity

        '''
        header = (
                f"capacity  : {self._capacity}\n"
                f"count     : {self._count}\n"
                f"load      : {load_factor:.2f}\n"
                )
        '''

        pairs = {
                index: node.value
                for index, node in enumerate(self._buckets)
                if node is not None
                }

        #return header + str(pairs)
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
        ''' Inserts a Node into the appropriate bucket. Also resizes the list of
            buckets if the next insertion reaches, or exceedes, the MAX_Load.

            The count instance variable is not owned here because multiple
            functions call self._insert() which is a more natural owner.
        
            self._count + 1 is passed to self._is_resize_required() to consider
            the current Node being set.
        '''
        if self._is_resize_required(self._count + 1, self._capacity):
            self._resize()

        self._insert(value)


    def get(self, target: Any) -> Any:
        index = self._scan(target)

        if index == -1 or index == -2:
            raise ValueError(f'{target} not found')
        else:
            return self._buckets[index].value


    def delete(self, target: Any) -> Any:
        index = self._scan(target)

        if index == -1 or index == -2:
            raise ValueError(f'{target} not found')
        else:
            self._buckets[index] == None
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


    def _next_empty_bucket(self, index: int) -> int:
        '''
        Called on a collision to lineraly probe for the next empty bucket.
        The ValueError here should never raise before resize is called.
        '''
        start = index
        next = self._get_next_index(start)

        while next != start:
            if self._buckets[next]== None:
                return next
            next = self._get_next_index(next)

        raise ValueError('All buckets are full')


    #TODO:
    #def _scan(self, start: int, target: Any | None = None) -> int:
        ''' Linear search for target value from starting index.
            Omit the target parameter to scan for the next empty bucket.
        '''
    def _scan(self, target: Any) -> int:
        ''' This is temporary until I can fold _next_empty_bucket into scan.
            
            Linear search by index for target value and returns index.
        '''
        index = self._hash(str(target))
        #result = self._buckets[index].value
        bucket = self._buckets[index]
        if not bucket:
            return -1

        result = bucket.value

        if result == target:
            return index
        elif result is None:
            return -1
        else:
            next = self._get_next_index(index)

            while next != index:
                if self._buckets[next].value == target:
                    return next
                next = self._get_next_index(next)

        return -2


    def _get_next_index(self, index: int) -> int:
        ''' Increment index with wrap from last to first index.
        '''
        return (index + 1) % self._capacity


    def _insert(self, value: Any) -> None:
        ''' Assigns a new Node to the hashed bucket unless there is a collision.
            In the event of a collision, the next empty bucket will be selected.
            Incrementing the count instance variable is owned here because the
            resize helper calls this instead of set. I admit this is a break
            from the single purpose principle.
        '''
        node = Node(value)
        index = self._hash(str(value))
        existing_value = self._buckets[index]

        if existing_value is None:
            self._buckets[index] = node
        else:
            self._buckets[self._next_empty_bucket(index)] = node

        # Incrementing this variable here because _resize calls this function
        self._count += 1


    def _is_resize_required(self, count: int, capacity: int) -> bool:
        load_factor = count / capacity
        return True if load_factor >= HashSet.MAX_LOAD else False


    def _resize(self) -> None:
        ''' Doubles capacity and rehash.
        '''
        # change in place -- hopefully 
        old_buckets = self._buckets
        new_capacity = self._capacity * 2
        self._buckets = [None] * new_capacity
        self._capacity = new_capacity
        self._count = 0

        for b in old_buckets:
            if b is not None:
                self._insert(b.value)


if __name__ == "__main__":
    hs = HashSet()
    hs.set(1)
    hs.set(0)
    hs.set(6)
    print(hs)
    print(repr(hs))
    print(f'got value {hs.get(1)}')
