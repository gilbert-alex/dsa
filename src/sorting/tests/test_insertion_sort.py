import pytest
from ..sorts import  Sorts


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
