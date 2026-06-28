import pytest
from ..sorts import  Sorts


@pytest.fixture
def sample_array():
    a = [42, 20, 17, 13, 28, 14, 23, 15]
    return a
    

@pytest.fixture
def sorted_ascending_array():
    a = [1, 2, 3, 4, 5]
    return a


@pytest.fixture
def sorted_descending_array():
    a = [5, 4, 3, 2, 1]
    return a


@pytest.fixture
def duplicates_array():
    a = [1, 5, 4, 4, 3, 2, 3]
    return a


@pytest.fixture
def negatives_array():
    a = [-1, 2, 0, -1, -2]
    return a


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


    @pytest.mark.parametrize('unordered, ordered', [
    ([42, 20, 17, 13, 28, 14, 23, 15], [13, 14, 15, 17, 20, 23, 28, 42]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 4, 3, 3], [1, 3, 3, 4]),
    ([2, 1, 0, -1, -2], [-2, -1, 0, 1, 2]),
    ])
    def test_sorts_various(self, unordered, ordered):
        s = Sorts()
        assert s.insertion_sort(unordered) == ordered
        

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
