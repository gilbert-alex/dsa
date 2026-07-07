import pytest
from ..hashmap import HashMap


@pytest.fixture
def default_hm():
    return HashMap()


def _make_hm(item_list):
    ''' This purposefully avoides hashing the keys to make for easier test setup.
    '''
    hm: HashMap = HashMap()
    counter = 0
    for outer_index, inner_list in enumerate(item_list):
        for inner_index, item in enumerate(inner_list):
            hm._buckets[outer_index].append(item)
            counter += 1
    hm._size = counter
    return hm


@pytest.fixture
def full_hm():
    item_list = [[('0', 0)], [('a', 1)], [('b', 2)], 
                 [('c', 3)], [('d', 4)],
                ]
    hm = _make_hm(item_list)
    return hm


@pytest.fixture
def oversize_hm():
    item_list = [[('0', 0)], [('a', 1)], [('b', 2)], 
                 [('c', 3)], [('d', 4)], [('e', 5)],
                ]
    hm = _make_hm(item_list)
    return hm


@pytest.fixture
def collision_hm():
    item_list = [[('0', 1), ('h', 2)]]      # mimic a collision
    hm = _make_hm(item_list)
    return hm


class TestSetup:
    def test_hm_maker(self):
        l = [[('a', 1)], [('b', 2)], [('c', 3)]]
        hm = _make_hm(l)
        assert len(hm) == 3
        print(hm._buckets)
        assert hm._buckets[0][0] == ('a', 1)
        assert hm._buckets[7] == []


    def test_default_hm(self, default_hm):
        hm = default_hm
        assert len(hm) == 0
        assert hm._capacity == 8
        assert hm._load_threshold == .75
        assert len(hm._buckets) == 8


    def test_full_hm(self, full_hm):
        hm = full_hm
        assert len(hm) == 5
        assert hm._capacity == 8
        assert hm._load_threshold == .75
        assert len(hm._buckets) == 8


class TestHash:
    @pytest.mark.parametrize('strings, expected', [
        ('0', 0),
        ('7', 7),
        ('8', 0),
        ('`', 0),
        ('a', 1),
        ('h', 0),
    ])
    def test_wrap(self, strings, expected, default_hm):
        hm = default_hm
        assert hm._hash(strings) == expected


class TestResize:
    def test_auto_resize(self, full_hm):
        hm = full_hm
        hm.put('z', 26)
        assert len(hm) == 6
        assert hm._capacity == 16

    
    def test_not_full_does_not_resize(self, default_hm):
        item_list = [('0', 0), ('a', 1), ('b', 2), 
                     ('c', 3), ('d', 4),
                    ]
        hm = default_hm
        for k, v in item_list:
            hm.put(k, v)
            assert hm._size / hm._capacity < hm._load_threshold
            assert hm._capacity == 8
            print(f'k:{k}, v:{v}')


    def test_threshold_for_resize(self, full_hm):
        hm = full_hm
        assert hm._size / hm._capacity < hm._load_threshold
        hm.put('z', 26)
        assert hm._size / hm._capacity < hm._load_threshold


    def test_hm_attributes_after_resize(self, full_hm):
        hm = full_hm
        assert len(hm) == 5
        assert hm._capacity == 8
        assert hm._load_threshold == 0.75
        hm.put('z', 26)
        assert len(hm) == 6
        assert hm._capacity == 16
        assert hm._load_threshold == 0.75


    def test_add_to_oversized_will_resize(self, oversize_hm):
        hm = oversize_hm
        assert hm._size == 6
        assert hm._size / hm._capacity >= hm._load_threshold
        hm.put('z', 26)
        assert hm._size == 7
        assert hm._size / hm._capacity <= hm._load_threshold
        

class TestPut:
    def test_add_to_empty_bucket(self, default_hm):
        hm = default_hm
        hm.put('a', 1)
        index = hm._hash('a')
        assert len(hm) == 1
        assert len(hm._buckets) == 8    # this is still the max bucket capacity
        assert len(hm._buckets[index]) == 1


    def test_add_with_collision(self, default_hm):
        hm = default_hm
        first_key = 'a'
        collision_key = chr(ord(first_key) + hm._capacity)
        hm.put('a', 1)
        hm.put('i', 2)
        index = hm._hash('a')
        assert len(hm) == 2
        assert len(hm._buckets) == 8    # capacity is still unchanged
        assert len(hm._buckets[index]) == 2


    def test_reset_existing_key(self, default_hm):
        k = 'a'
        v1 = 1
        v2 = 2
        hm = default_hm
        hm.put(k, v1)
        hm.put(k, v2)
        index = hm._hash(k)
        assert len(hm) == 1
        assert len(hm._buckets) == 8
        assert len(hm._buckets[index]) == 1
        assert hm._buckets[index][0] == (k, v2) 


    @pytest.mark.parametrize('key, value', [
        ('a', 1),
        ('a', 'b'),
        ('message', 'words and stuff'),
        ('nothing', None),
        ('empty', ''),
    ])
    def test_put_typical_datatypes(self, default_hm, key, value):
        hm = default_hm
        hm.put(key, value)
        index = hm._hash(key)
        assert hm._buckets[index][0] == (key, value)


class TestGet:
    def test_get_existing_value(self, full_hm):
        hm = full_hm
        print(hm._buckets)
        print(hm._hash('a'))
        assert hm.get('a') == 1


    def test_get_non_existing_value(self, default_hm):
        hm = default_hm
        assert hm.get('a') == None


    def test_get_passed_default_value(self, default_hm):
        hm = default_hm
        assert hm.get('a', 'not here') == 'not here'


    def test_get_from_collision(self, collision_hm):
        hm = collision_hm
        assert hm.get('0') == 1 
        assert hm.get('h') == 2


class TestRemove:
    def test_remove_returns_tuple(self, full_hm):
        hm = full_hm
        assert hm.remove('a') == ('a', 1)


    def test_remove_not_found_returns_false(self, full_hm):
        hm = full_hm
        assert hm.remove('z') == False


class TestContains:
    def test_found_key_returns_true(self, full_hm):
        hm = full_hm
        assert hm.contains('a') == True


    def test_not_found_key_returns_false(self, full_hm):
        hm = full_hm
        assert hm.contains('z') == False


    def test_finds_key_in_collision(self, collision_hm):
        hm = collision_hm
        assert hm.contains('0') == True
        assert hm.contains('h') == True


class TestComponent:
    def test_hash_map(self):
        teams: HashMap = HashMap()
        assert teams._capacity == 8
        assert len(teams) == 0
        teams.put('Mexico', 'Group A')
        teams.put('South Africa', 'Group A')
        teams.put('South Korea', 'Group A')
        teams.put('Czechia', 'Group A')
        assert len(teams) == 4
        teams.put('Antartica', 'surprise')
        assert teams.contains('United States') == False
        removed = teams.remove('Antartica')
        assert removed == ('Antartica', 'surprise')
        assert len(teams) == 4
        teams.put('Canada', 'Group B')
        teams.put('Hosnia-Herzegovina', 'Group B')
        teams.put('Qatar', 'Group B')
        teams.put('Switzerland', 'Group B')
        assert teams._capacity == 16
        assert len(teams) == 8
