import pytest
from ..sorts import  Sorts


@pytest.fixture
def sample_array():
    return [42, 20, 17, 13, 28, 14, 23, 15]


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


    def test_sorted_array_returns_unchanged(self):
        s = Sorts()
        a: list[int] = [10, 20, 30, 40]
        assert s.insertion_sort(a) == a


    def test_array_mutated_inplace(self):
        s = Sorts()
        a: list[int] = []
        initial_addr = id(a)
        assert id(s.insertion_sort(a)) == initial_addr


    def test_sort_yields_ascending_array(self, sample_array):
        s = Sorts()
        sorted_array = sorted(sample_array)
        result = s.insertion_sort(sample_array)
        assert result == sorted_array
