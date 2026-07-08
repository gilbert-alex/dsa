import random
import statistics 


import pytest
from ..quadratic_sorts import  Sorts


@pytest.fixture
def sample_array():
    return [42, 20, 17, 13, 28, 14, 23, 15]


@pytest.fixture
def sorted_ascending_array():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sorted_descending_array():
    return [5, 4, 3, 2, 1]


@pytest.fixture
def duplicates_array():
    return [1, 5, 4, 4, 3, 2, 3]


@pytest.fixture
def negatives_array():
    return [1, 2, 0, -2, -1]


@pytest.fixture
def scattered_array():
    return [10, 20, 15, 30, 25]


@pytest.fixture
def more_scattered_array():
    return [8, 3, 7, 1, 5, 2, 6, 4]


@pytest.fixture
def list_of_dictionaries():
    return [
        {'name': 'baz', 'amount': 100},
        {'name': 'foo', 'amount': 10},
        {'name': 'bar', 'amount': 50},
    ]

class TestSwap():
    def test_swap_high_to_low_index(self):
        s = Sorts()
        assert s._swap([10, 20, 30], 0, 2) == [30, 20, 10]


    def test_swap_low_to_high_index(self):
        s = Sorts()
        assert s._swap([10, 20, 30], 1, 0) == [20, 10, 30]


    def test_swap_increments_counter(self):
        s = Sorts()
        count_before: int = s._swap_count
        s._swap([10, 20], 0, 1)
        assert s._swap_count == count_before + 1


class TestInsertionSort():
    def test_empty_array_returns_empty(self):
        s = Sorts()
        assert s.insertion_sort([]) == []


    def test_array_mutated_inplace(self):
        s = Sorts()
        a: list[int] = []
        initial_addr = id(a)
        assert id(s.insertion_sort(a)) == initial_addr


    @pytest.mark.parametrize('unsorted_fixture', [
        'sample_array',
        'sorted_ascending_array',
        'sorted_descending_array',
        'duplicates_array',
        'negatives_array',
    ])
    def test_fixture_invariants(self, unsorted_fixture, request):
        array = request.getfixturevalue(unsorted_fixture)
        s = Sorts()
        result = s.insertion_sort(array)
        assert all(l <= r for l, r in zip(result, result[1:]))


    @pytest.mark.parametrize('unsorted_fixture, expected', [
        ('sample_array', 18),
        ('sorted_ascending_array', 0),
        ('sorted_descending_array', 10),
        ('duplicates_array', 12),
        ('negatives_array', 8),
        ('scattered_array', 2),
        ('more_scattered_array', 17),
    ])
    def test_swap_count(self, unsorted_fixture, request, expected):
        array = request.getfixturevalue(unsorted_fixture)
        s = Sorts()
        s.insertion_sort(array)
        assert s._swap_count == expected


    @pytest.mark.parametrize('size', [10, 50, 100])
    def test_average_case_compares(self, size):
        ''' Compares Average Case: (n(n-1)/4)+n 
            - n: outer loop
            - n-1: inner loop except 0-th index
            - /4: 0-th to (i-1)-th indicies are sorted and an element only
              moves left to it's sorted position. /2 is worst case but 
              /4 on average. 
            - +n: one additional while loop conditional call per outer loop
            - 15% expected count allowed
        '''
        s = Sorts()
        compares_list: list[int] = []

        for _ in range(100):
            array: list[int] = list(range(size))
            random.shuffle(array)
            s.insertion_sort(array)
            compares_list.append(s._compare_count)

        avg_compares = statistics.mean(compares_list)
        exp_compares = (size*(size-1)/4)+size
        print(f'size: {size}; avg: {avg_compares}; exp: {exp_compares}')
        assert abs(avg_compares - exp_compares) < exp_compares * 0.15


    @pytest.mark.parametrize('size', [10, 50, 100])
    def test_average_case_swaps(self, size):
        ''' Swaps Average Case: n(n-1)/4 
            - n: outer loop
            - n-1: inner loop except 0-th index
            - /4: 0-th to (i-1)-th indicies are sorted and an element only
              moves left to it's sorted position. /2 is worst case but 
              /4 on average. 
            - 15% expected count allowed
        '''
        s = Sorts()
        swaps_list: list[int] = []

        for _ in range(100):
            array: list[int] = list(range(size))
            random.shuffle(array)
            s.insertion_sort(array)
            swaps_list.append(s._swap_count)

        avg_swaps = statistics.mean(swaps_list)
        exp_swaps = size*(size-1)/4
        print(f'size: {size}; avg: {avg_swaps}; exp: {exp_swaps}')
        assert abs(avg_swaps - exp_swaps) < exp_swaps * 0.15


    def test_dictionary_sort(self, list_of_dictionaries):
        expected = [
            {'name': 'foo', 'amount': 10},
            {'name': 'bar', 'amount': 50},
            {'name': 'baz', 'amount': 100},
        ]
        s = Sorts()
        assert s.insertion_sort(
            list_of_dictionaries, 
            key=lambda record: record['amount']
        ) == expected


class TestBubbleSort():
    def test_empty_array_returns_empty(self):
        s = Sorts()
        assert s.bubble_sort([]) == []


    def test_array_mutated_inplace(self):
        s = Sorts()
        a: list[int] = []
        initial_addr = id(a)
        assert id(s.bubble_sort(a)) == initial_addr


    @pytest.mark.parametrize('unsorted_fixture', [
        'sample_array',
        'sorted_ascending_array',
        'sorted_descending_array',
        'duplicates_array',
        'negatives_array',
    ])
    def test_fixture_invariants(self, unsorted_fixture, request):
        array = request.getfixturevalue(unsorted_fixture)
        s = Sorts()
        result = s.bubble_sort(array)
        assert all(l <= r for l, r in zip(result, result[1:]))


    @pytest.mark.parametrize('unsorted_fixture, expected', [
        ('sample_array', 18),
        ('sorted_ascending_array', 0),
        ('sorted_descending_array', 10),
        ('duplicates_array', 12),
        ('negatives_array', 8),
        ('scattered_array', 2),
        ('more_scattered_array', 17),
    ])
    def test_swap_count(self, unsorted_fixture, request, expected):
        array = request.getfixturevalue(unsorted_fixture)
        s = Sorts()
        s.bubble_sort(array)
        assert s._swap_count == expected


    @pytest.mark.parametrize('size', [10, 50, 100])
    def test_average_case_compares(self, size):
        ''' Compares Average Case: n(n-1)/2 
            - n: outer loop
            - n-1: inner loop except last index which will be the max
              value by default.
            - /2: as the outer loop iterates the sorted subarray limits
              the max distance necessary to move a value.
            - The count of compares is known because all options are 
              compared in every loop iteration.
        '''
        s = Sorts()
        compares_list: list[int] = []

        for _ in range(100):
            array: list[int] = list(range(size))
            random.shuffle(array)
            s.bubble_sort(array)
            compares_list.append(s._compare_count)

        avg_compares = statistics.mean(compares_list)
        exp_compares = size*(size-1)/2
        print(f'size: {size}; avg: {avg_compares}; exp: {exp_compares}')
        assert avg_compares == exp_compares


    @pytest.mark.parametrize('size', [10, 50, 100])
    def test_average_case_swaps(self, size):
        ''' Swaps Average Case: n(n-1)/4 
            - n: outer loop
            - n-1: inner loop except last index which will be the max
              value by default.
            - /4: as the outer loop iterates the sorted subarray limits
              the max distance necessary to move a value. Worst case is 
              /2 but average is /4.
            - 15% expected count allowed
        '''
        s = Sorts()
        swaps_list: list[int] = []

        for _ in range(100):
            array: list[int] = list(range(size))
            random.shuffle(array)
            s.bubble_sort(array)
            swaps_list.append(s._swap_count)

        avg_swaps = statistics.mean(swaps_list)
        exp_swaps = size*(size-1)/4
        print(f'size: {size}; avg: {avg_swaps}; exp: {exp_swaps}')
        assert abs(avg_swaps - exp_swaps) < exp_swaps * 0.15


class TestSelectionSort():
    def test_empty_array_returns_empty(self):
        s = Sorts()
        assert s.selection_sort([]) == []


    def test_array_mutated_inplace(self):
        s = Sorts()
        a: list[int] = []
        initial_addr = id(a)
        assert id(s.selection_sort(a)) == initial_addr


    def test_debug(self):
        s = Sorts()
        a: list[int] = [4, 3, 2, 1]
        s.selection_sort(a)
        assert a == [1, 2, 3, 4]

    @pytest.mark.parametrize('unsorted_fixture', [
        'sample_array',
        'sorted_ascending_array',
        'sorted_descending_array',
        'duplicates_array',
        'negatives_array',
    ])
    def test_fixture_invariants(self, unsorted_fixture, request):
        array = request.getfixturevalue(unsorted_fixture)
        s = Sorts()
        result = s.selection_sort(array)
        assert all(l <= r for l, r in zip(result, result[1:]))
