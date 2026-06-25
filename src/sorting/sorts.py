class Sorts():
    def __init__(self):
        self._swap_count = 0


    def _swap(self, array: list[int], left: int, right: int):
        buffer: int = array[left]
        array[left] = array[right]
        array[right] = buffer
        self._swap_count += 1
        return array


    def _right_greater_than(self, left: int, right: int):
        return True if right > left else False


    def insertion_sort(self, array: list[int]) -> list[int]:
        ''' Sorts, in place, an array of integers in ascending order.

        Pseudocode: 
            For each integer in array, backtrack and swap any inverted values
            until a greater or equal value, or the beginning of the array, 
            is encountered.

        Observations: 
            - Could skip the outer loop's first position but would require
              a for loop with i = 1.
            - A sorted ascending array prevents the inner loop for executing 
              and gives a best-case runtime of O(n).
            - The risk of worst-case may be acceptable if the ordering
              of the input array is controlled. A nearly-sorted ascending
              array would result in a less than average runtime of O(n2) time
              as fewer positions are inverted.
                - See Shellsort and Quicksort algorithms
        '''

        self._swap_count = 0

        for i in range(len(array)):
            if i == 0:
                continue

            current: int = i
            previous: int = i - 1

            while current > 0 and array[current] < array[previous]:
                self._swap(array, current, previous)
                current -= 1
                previous -= 1

        return array


if __name__ == '__main__':
    l = [3, 2, 1]
    print(f'original: {l}')
    s = Sorts()
    print(f'sorted: {s.insertion_sort(l)}')
