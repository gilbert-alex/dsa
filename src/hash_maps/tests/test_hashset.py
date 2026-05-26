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


def _make_hs(item_list):
    hs = HashSet()
    hs._count = len(item_list)
    for index, value in enumerate(item_list):
        hs._buckets[index] = value
    return hs


class TestSet:
    def test_set_as_component(self, default_hs):
        hs = default_hs

        capacity_default = hs._capacity
        count_default = hs._count
        assert capacity_default == 8
        assert count_default == 0
        assert len(hs._buckets) == 8

        for i in range(0, 5):
            hs.set(i)
        assert hs._count == 5
        
        hs.set('this should cause a resize')
        assert hs._capacity == capacity_default * 2
        assert hs._count == 6


class TestGet:
    @pytest.mark.parametrize('strings, target, expected', [
        (range(0, 8), 0, 0),          # first index
        (range(0, 8), 7, 7),          # last index
        (range(0, 8), 2, 2),          # start in middle
        (range(0, 8), 1, 1),          # wraps
    ])
    def test_get_returns_found(self, strings, target, expected):
        hs = _make_hs(strings)
        assert hs.get(target) == expected


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
        (range(0, 1), 0, 1),
        (range(0, 7), 0, 7),
        ([0, 1, 2, 3, None, 5, 6, 7], 0, 4),      # 5th index
        ([0, None, 2, 3, 4, 5, None, 7], 2, 6),         # search right
        ([None, 1, 2, 3, 4, 5, 6, 7], 1, 0),      # wraps
    ])
    def test_find_empty_bucket(self, strings, index, expected):
        hs = _make_hs(strings)
        assert hs._find_empty_bucket(index) == expected

    
    def test_full_buckets_raise(self):
        hs = _make_hs(range(0, 8))
        with pytest.raises(ValueError):
            hs._find_empty_bucket(0)


class TestScan:
    @pytest.mark.parametrize('strings, start, target, expected', [
        (range(0, 8), 1, 0, 0),          # return first index
        (range(0, 8), 0, 7, 7),          # return last index
        (range(0, 8), 1, 2, 2),          # start in middle
        (range(0, 8), 4, 1, 1),          # wraps
    ])
    def test_scan(self, strings, start, target, expected):
        hs = _make_hs(strings)
        assert hs._scan(start, target) == expected


    def test_scan_not_return_start(self):
        hs = _make_hs(range(0, 7))
        with pytest.raises(ValueError):
            hs._scan(0, 0)


    def test_scan_not_wrap_to_start(self):
        hs = _make_hs(range(0, 7))
        with pytest.raises(ValueError):
            hs._scan(2, 2)


    def test_scan_for_empty_bucket(self):
        item_list = [0, 1, 2, None, 3, 4, 5]
        hs = _make_hs(item_list)
        assert hs._scan(0, None) == 3


    def test_full_buckets_raise(self):
        hs = _make_hs(range(0, 8))
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
        hs = _make_hs(range(4))
        assert hs._get_next_index(index) == expected


class TestInsert:
    def test_insert_increments_count(self, default_hs):
        before = len(default_hs)
        default_hs._insert('a')
        after = len(default_hs)
        assert after == before + 1

        
    def test_insert_to_empty_hs(self, default_hs):
        default_hs._insert('test')
        assert len(default_hs) == 1


    def test_insert_duplicate_values(self, default_hs):
        for s in ['test'] * 2:
            default_hs._insert(s)
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
    def test_insert_datatypes(self, values, default_hs):
        default_hs._insert(values)
        assert len(default_hs) == 1


class TestMeasureLoadFactor:
    @pytest.mark.parametrize('count, capacity, expected', [
        (0, 8, False),         # empty
        (5, 8, False),         # max load acceptable
        (6, 8, True),          # reaches max load
    ])
    def test_load_measurement_signal(self, count, capacity, expected, default_hs):
        assert default_hs._is_resize_required(count, capacity) == expected


