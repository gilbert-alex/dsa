''' Should this be implemented as a function with helpers like _swap?
    or should it be a class?
'''


def _swap(array: list[int], a: int, b: int):
    buffer: int = array[a]
    array[a] = array[b]
    array[b] = buffer
    return array


def insertion_sort(array: list[int]) -> list[int]:

    for i in range(len(array)):
        if i == 0:
            continue

        current: int = i
        previous: int = i - 1

        while current > 0 and array[current] < array[previous]:
            _swap(array, current, previous)
            current -= 1
            previous -= 1

    return array


if __name__ == '__main__':
    l = [3, 2, 1]
    print(f'original: {l}')
    print(f'sorted: {insertion_sort(l)}')
