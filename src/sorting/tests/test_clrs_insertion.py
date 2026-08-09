import pytest
from ..clrs_insertion_sort import insertion_sort


class TestCLRSInsertionSort():

    @pytest.mark.parametrize('array', [
        [5, 4, 3, 2, 1],
        [20, 10, 50, 30, 20],
        [],
        [1],
        [1, 2],
    ])
    def test_clrs_insertion_sort(self, array):
        assert insertion_sort(array, len(array)) == sorted(array)
