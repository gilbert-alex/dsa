class Sorts():
    def __init__(self):
        self._swap_count = 0
        self._compare_count = 0


    def _swap(self, array: list[int], left: int, right: int):
        buffer: int = array[left]
        array[left] = array[right]
        array[right] = buffer
        self._swap_count += 1
        return array


    def _compare(self, target: int, compare: int):
        ''' Returns True if arg1 < arg2.
        '''
        self._compare_count += 1
        return True if target < compare else False


    def insertion_sort(self, array: list[int], key = lambda x: x) -> list[int]:
        self._swap_count = 0
        self._compare_count = 0

        for i in range(1, len(array)):
            current: int = i
            previous: int = i - 1

            while current > 0 and self._compare(key(array[current]), key(array[previous])):
                self._swap(array, current, previous)
                current -= 1
                previous -= 1

        return array


    def bubble_sort(self, array: list[int]) -> list[int]:
        self._swap_count = 0
        self._compare_count = 0

        length = len(array)
        for i in range(length):
            for j in range(length-1, i, -1):
                if self._compare(array[j], array[j-1]):
                    self._swap(array, j, j-1)

        return array 


if __name__ == '__main__':
    l = [3, 2, 1]
    m = [1, 2, 3]

    s = Sorts()
    #s.insertion_sort(l) print(s.bubble_sort(m))
    print(s.bubble_sort(l))
