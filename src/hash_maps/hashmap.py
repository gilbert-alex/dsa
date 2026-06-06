class HashMap:

    DEFAULT_CAPACITY = 8
    LOAD_THRESHOLD = 0.75


    def __init__(self, 
                 capacity = DEFAULT_CAPACITY, 
                 load_threshold = LOAD_THRESHOLD):
        self._capacity = capacity
        self._load_threshold = load_threshold
        self._size = 0
        self._buckets = [[] for _ in range(self._capacity)]


    def _hash(self, value: str) -> int:
        ''' Intentionally simple for easier tests. 
            Include a prime multiplication factor to improve distribution.
        '''
        buffer = 0
        chars = list(value)

        for char in chars:
            buffer = (buffer + ord(char.lower())) % self._capacity
        return buffer


    def put(self, key, value):
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, v)
                return

        bucket.append((key, value))
        self._size += 1


    def get(self, key, default = None):
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return default


    def remove(self, key):
        pass


    def contains(self, key):
        pass
    

    def __len__(self):
        return self._size
