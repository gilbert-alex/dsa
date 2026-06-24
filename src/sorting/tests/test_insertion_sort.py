import pytest
from ..insertion import  _swap, insertion_sort


@pytest.fixture
def sample_array():
    return [42, 20, 17, 13, 28, 14, 23, 15]


class TestSwap():
    def test_swap_a_to_b(self):
        assert _swap([10, 20, 30], 0, 2) == [30, 20, 10]


    def test_swap_b_to_a(self):
        assert _swap([10, 20, 30], 1, 0) == [20, 10, 30]


class TestInsertionSort():
    def test_empty_array_returns_empty(self):
        assert insertion_sort([]) == []


    def test_sorted_array_returns_unchanged(self):
        a = [10, 20, 30, 40]
        assert insertion_sort(a) == a


    def test_array_mutated_inplace(self):
        a: list[int] = []
        initial_addr = id(a)
        assert id(insertion_sort(a)) == initial_addr


    def test_sorts_asc(self, sample_array):
        sorted_array = sorted(sample_array)
        result = insertion_sort(sample_array)
        assert result == sorted_array
