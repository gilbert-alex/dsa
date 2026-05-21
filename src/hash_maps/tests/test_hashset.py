import pytest
from ..hashset import Node, HashSet


@pytest.fixture
def default_hs():
    return HashSet()


@pytest.fixture
def hs_100():
    return HashSet(100)


def _make_hs(*items):
    hs = HashSet()
    hs._len = len(items)
    for i in items:
        hs._buckets[i] = i
    return hs


class TestSet:
    def test_set_to_empty_hs(self, default_hs):
        pass


class TestHash:
    @pytest.mark.parametrize('values, expected', [
        ('a', 1),
        ('A', 1),
        ('b', 2),
        ('B', 2),
        ('z', 2),
        ('ab', 3),
        ('0', 0),
        ('1', 1),
        ('012', 3),
        (' ', 0),
    ])
    def test_default_hash(self, values, expected, default_hs):
        assert default_hs._hash(values) == expected


    @pytest.mark.parametrize('values, expected', [
        ('apple', 30),
    ])
    def test_small_hash(self, values, expected, hs_100):
        assert hs_100._hash(values) == expected


class TestFindEmptyBucket:
    @pytest.mark.parametrize('values, index, expected', [
        ([], 0, 1),                         # expected [1] not [0]
        ([*range(0, 1)], 0, 1),
        ([*range(0, 7)], 0, 7),
        ([0, 1, 2, 3, 5, 6, 7], 0, 4),      # 4th index
        ([0, 2, 3, 4, 5, 7], 2, 6),         # search right
        ([1, 2, 3, 4, 5, 6, 7], 1, 0),      # wraps
    ])
    def test_find_empty_bucket(self, values, index, expected):
        hs = _make_hs(*values)
        assert hs._find_empty_bucket(index) == expected

    
    def test_full_buckets_raise(self):
        hs = _make_hs(*range(0,8))
        with pytest.raises(ValueError):
            hs._find_empty_bucket(0)


class TestGetNextIndex:
    @pytest.mark.parametrize('index, expected', [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 0),
    ])
    def test_get_next_bucket(self, index, expected):
        hs = _make_hs(*range(4))
        assert hs._get_next_index(index) == expected
