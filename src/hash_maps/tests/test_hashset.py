import pytest
import random
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
        if value == None:
            continue
        else:
            n = Node(value)
            hs._buckets[index] = n
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


class TestDelete:
    @pytest.mark.parametrize('strings, target, expected', [
        (range(0, 8), 0, [None, 1, 2, 3, 4, 5, 6, 7]),
        ([None, 1, 2, 3], 1, [None, None, 2, 3]),
    ])
    def test_delete_removes_node(self, strings, target, expected):
        hs = _make_hs(strings)
        hs.delete(target)
        hs._buckets == expected


    def test_delete_decrements_length(self, default_hs):
        hs = default_hs
        for item in [1, 2, 3]:
            hs.set(item)
        hs.delete(1)
        assert len(hs) == 2


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
        ([], 0, 0),
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
    @pytest.mark.parametrize('strings, target, expected', [
        (range(0, 8), 0, 0),          # return first index
        (range(0, 8), 7, 7),          # return last index
        (range(0, 8), 2, 2),          # start in middle
    ])
    def test_scan_for_target_expected_behavior(self, strings, target, expected):
        hs = _make_hs(strings)
        assert hs._scan_for_target(target) == expected


    ''' The _make_hs function does not hash inputs. So, the ordering of the 
        values here mimics the result of a collision. _scan_for_target will still initiate
        it's search from the target's hashed index.
    '''
    @pytest.mark.parametrize('values, target, expected', [
        ([0, 8], 8, 1),
        ([0, 8, 1], 1, 2),
        ([0, 8, 2, 17], 17, 3),
    ])
    def test_scan_for_target_with_colision(self, values, target, expected):
        hs = _make_hs(values)
        assert hs._scan_for_target(target) == expected


    def test_scan_for_target_with_wrap(self):
        values = [2, 3, 4, 5, 6, 7, 0, 1]
        hs = _make_hs(values)
        assert hs._scan_for_target(2) == 0

    
    def test_scan_for_target_not_found_code(self):
        hs = _make_hs(range(0, 8))
        assert hs._scan_for_target(8) == None


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


class TestComponent:
    def test_component(self):
        cruise_stops = HashSet()
        assert cruise_stops._capacity == 8
        assert len(cruise_stops) == 0
        cruise_stops.set('Vancouver')
        cruise_stops.set('Ketchikan')
        cruise_stops.set('Icy Strait Point')
        cruise_stops.set('Sitka')
        cruise_stops.set('Skagway')
        assert cruise_stops._capacity == 8
        assert len(cruise_stops) == 5
        cruise_stops.set('Hubbard Glacier')
        assert cruise_stops._capacity == 16
        assert len(cruise_stops) == 6
        cruise_stops.set('Seward')
        assert cruise_stops.get('Skagway') == 'Skagway'
        with pytest.raises(ValueError):
            cruise_stops.get('Homer')
        cruise_stops.delete('Vancouver')
        print(cruise_stops)
        assert len(cruise_stops) == 6


    def test_tombstone(self):
        hs = HashSet()
        hs.set(0)
        index_0 = hs._scan_for_target(0)
        hs.set(8)   # collision
        hs.delete(0)
        assert hs._buckets[index_0] == hs._TOMBSTONE
        assert hs._scan_for_target(8) == index_0 + 1
        hs.set(0)
        assert hs._scan_for_target(0) == 0


    def test_tombstone_reclaimed_through_resize(self):
        hs = HashSet()
        first_set = random.sample(range(-100, 100), 10)
        for value in first_set:
            hs.set(value)

        assert hs._capacity == 16
        assert len(hs) == 10
        for value in first_set:
            assert hs.get(value) == value

        for value in first_set:
            hs.delete(value)

        assert hs._capacity == 16
        assert len(hs) == 0
        for value in first_set:
            with pytest.raises(ValueError):
                hs.get(value)

        second_set = random.sample(range(-100, 100), 12)
        for value in second_set:
            hs.set(value)

        assert hs._capacity == 32
        assert len(hs) == 12
        for value in second_set:
            assert hs.get(value) == value

