from typing import Any, Generic, TypeAlias, TypeVar


T = TypeVar('T')
BucketType: TypeAlias = list[tuple[str, T]]
HashmapType: TypeAlias = list[BucketType] 

class HashMap(Generic[T]):

    DEFAULT_CAPACITY = 8
    LOAD_THRESHOLD = 0.75


    def __init__(self, 
                 capacity: int = DEFAULT_CAPACITY, 
                 load_threshold: float = LOAD_THRESHOLD) -> None:
        self._capacity: int = capacity
        self._load_threshold: float = load_threshold
        self._size: int = 0
        self._buckets: HashmapType = [[] for _ in range(self._capacity)]


    def _hash(self, value: str) -> int:
        ''' Intentionally simple for easier tests. 
            Include a prime multiplication factor to improve distribution.
        '''
        buffer: int = 0
        chars: list[str] = list(value)

        for char in chars:
            buffer = (buffer + ord(char.lower())) % self._capacity
        return buffer


    def _resize(self) -> None:
        old_buckets: HashmapType = self._buckets
        self._size = 0
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]

        for bucket in old_buckets:
            for k, v in bucket:
                self.put(k, v)


    def put(self, key: str, value: T) -> None:
        index: int = self._hash(key)
        bucket: BucketType = self._buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, value)
                return

        bucket.append((key, value))
        self._size += 1
        
        if self._load_threshold <= self._size / self._capacity:
            self._resize()


    def get(self, key: str, default: Any = None):
        index: int = self._hash(key)
        bucket: BucketType = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return default


    def remove(self, key: str) -> tuple | bool:
        index: int = self._hash(key)
        bucket: BucketType = self._buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                self._size -= 1
                return bucket.pop(i)

        return False


    def contains(self, key: str) -> bool:
        return False if not self.get(key) else True
    

    def __len__(self) -> int:
        return self._size
