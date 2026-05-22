import pytest
from ..hashset import Node, HashSet


@pytest.fixture
def default_hs():
    return HashSet()


@pytest.fixture
def hs_10():
    return HashSet(10)


@pytest.fixture
def hs_100():
    return HashSet(100)


@pytest.fixture
def hs_127():
    return HashSet(127)


def _make_hs(*items):
    hs = HashSet()
    hs._len = len(items)
    for i in items:
        hs._buckets[i] = i
    return hs


class TestSet:
    def test_set_increments_len(self, default_hs):
        before = len(default_hs)
        default_hs.set('a')
        after = len(default_hs)
        assert after == before + 1

        
    def test_set_to_empty_hs(self, default_hs):
        default_hs.set('test')
        assert len(default_hs) == 1


    def test_set_duplicate_values(self, default_hs):
        for s in ['test'] * 2:
            default_hs.set(s)
        assert len(default_hs) == 2


    @pytest.mark.parametrize('values', [
        ('string'),
        ('alphanumeric100'),
        (100),
        (-100),
        (1,000),
        (-1,000),
        (1),
        (0),
        (False),
        (True),
        (' '),
        (None),
    ])
    def test_set_datatypes(self, values, default_hs):
        default_hs.set(values)
        assert len(default_hs) == 1


class TestHash:
    @pytest.mark.parametrize('strings, expected', [
        ('0', 0),
        ('7', 7),
        ('8', 0),
    ])
    def test_wrap(self, strings, expected, default_hs):
        assert default_hs._hash(strings) == expected


    @pytest.mark.parametrize('strings, expected', [
        ('a', 97),
        ('A', 97),
        ('b', 98),
        ('B', 98),
        ('z', 122),
        ('Z', 122),
        ('0', 48),
        ('9', 57),
        (' ', 32),
    ])
    def test_ascii_characters(self, strings, expected, hs_127):
        assert hs_127._hash(strings) == expected


    @pytest.mark.parametrize('strings, expected', [
        ('0', 8), ('1', 9), ('2', 0), ('3', 1), ('4', 2), 
        ('5', 3), ('6', 4), ('7', 5), ('8', 6), ('9', 7),
        ('012', 7),
        ('123', 0),
    ])
    def test_numeric(self, strings, expected, hs_10):
        assert hs_10._hash(strings) == expected


    @pytest.mark.parametrize('strings, expected', [
        ('apple', 30),
        ('APPLE', 30),
    ])
    def test_words(self, strings, expected, hs_100):
        assert hs_100._hash(strings) == expected


    @pytest.mark.parametrize('strings, expected', [
        (' ', 32),
        ('two words', 37),
        ('hyphenated-word', 55),
        ("apostrophe's", 47),
    ])
    def test_edge_cases(self, strings, expected, hs_100):
        assert hs_100._hash(strings) == expected



class TestFindEmptyBucket:
    @pytest.mark.parametrize('strings, index, expected', [
        ([], 0, 1),                         # expected [1] not [0]
        ([*range(0, 1)], 0, 1),
        ([*range(0, 7)], 0, 7),
        ([0, 1, 2, 3, 5, 6, 7], 0, 4),      # 4th index
        ([0, 2, 3, 4, 5, 7], 2, 6),         # search right
        ([1, 2, 3, 4, 5, 6, 7], 1, 0),      # wraps
    ])
    def test_find_empty_bucket(self, strings, index, expected):
        hs = _make_hs(*strings)
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
