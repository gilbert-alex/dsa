class Queue:
    '''
    Implements a FIFO array which dequeues from the 0th index.
    This implementation of a queue operates at time complexity of O(1)
    insertion and O(n) for deletion due to the reindexing ("shifting")
    of every element upon deletion.
    
    This implementation uses a space complexity of O(2n) due to the 
    dequeue buffer.
    '''

    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        buffer = self._data[0]
        self._data = self._data[1::]
        return buffer

    def peek(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f"Queue({self._data})"

