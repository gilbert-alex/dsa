import pytest
from ..clrs_merge_sort import merge, merge_sort


class TestCLRSMergeSort():

    @pytest.mark.parametrize('before, after', [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
        ([2, 1, 3], [1, 2, 3]),
        ([5, 4, 3, 2, 1], [3, 2, 1, 5, 4]),
        ([20, 40, 10, 30, 50], [10, 20, 30, 40, 50]),
    ])
    def test_sort_mechanism(self, before, after):
        left: int = 0
        right: int = len(before)
        middle: int = int(right / 2)
        merge(before, left, middle, right)
        assert before == after

    @pytest.mark.parametrize('before, after', [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([8, 2, 4, 0, 1, 3, 7, 5, 6, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ])
    def test_sort(self, before, after):
        merge_sort(before, 0, len(before))
        assert before == after
