# CLRS: Introduction to Algorithms pg 36
import math


def merge(a: list[int], p: int, q: int, r: int):
    # find number of indicies on left and right of provided
    nl = q - p
    nr = r - q

    # init temp arrays
    al: list[int | None] = [None] * nl
    ar: list[int | None] = [None] * nr

    # fill temp arrays with left and right halves from origional
    for n in range(nl):
        al[n] = a[p + n]

    for n in range(nr):
        ar[n] = a[q + n]

    i = 0  # index of smallest remaining element in left temp array
    j = 0  # index of smallest remaining element in right temp array
    k = p  # index location in a to fill

    # while both temp arrays are not empty
    while i < nl and j < nr:
        vl = al[i]
        vr = ar[j]
        assert vl is not None
        assert vr is not None
        if vl <= vr:
            a[k] = vl
            i += 1
        else:
            a[k] = vr
            j += 1
        k += 1

    # when one temp array empties
    while i < nl:
        vl = al[i]
        assert vl is not None
        a[k] = vl
        i += 1
        k += 1
    while j < nr:
        vr = ar[j]
        assert vr is not None
        a[k] = vr
        j += 1
        k += 1

    return


def merge_sort(a: list[int], start: int, end: int) -> None:
    ''' Sort an array of integers in place. '''

    if start > end:
        raise IndexError(
            f'invalid arguments: starting index must be greater than or equal to the ending index. start:{start}, end:{end}'
        )

    # base case returns on lists of size 1 or 0
    if end - start <= 1:
        return

    midpoint = math.floor((start + end) / 2)
    merge_sort(a, start, midpoint)
    merge_sort(a, midpoint, end)

    merge(a, start, midpoint, end)
    return


if __name__ == '__main__':
    array = [4, 3, 2, 1]
    merge_sort(array, 0, len(array))
    print(array)
