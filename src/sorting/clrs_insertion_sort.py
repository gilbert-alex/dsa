# CLRS: Introduction to Algorithms pg 19


def insertion_sort(a: list[int], n: int) -> list[int]:
    for i in range(1, n):
        key = a[i]
        # insert a[i] into sorted subarray a[0: i-1]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key
    return a


if __name__ == "__main__":
    array = [1, 2, 3, 4]
    array = [8, 7, 6, 5]
    number = len(array)
    sorted = insertion_sort(array, number)
    print(sorted)
