import pytest
from ..hashmap import HashMap


@pytest.fixture
def default_hm():
    return HashMap()


def _make_hm(item_list):
    ''' This purposefully avoides hashing the keys to make for easier test setup.
    '''
    hm = HashMap()
    hm._size = len(item_list)
    for index, (key, value) in enumerate(item_list):
        hm._buckets[index] = (key, value)
    return hm


class TestSetup:
    def test_hm_maker(self):
        l = [('a', 1), ('b', 2), ('c', 3)]
        hm = _make_hm(l)
        print(hm._buckets)
        assert len(hm) == 3
        assert hm._buckets[0] == ('a', 1)
        assert hm._buckets[7] == []


class TestPut:
    def test_add_to_empty_bucket(self, default_hm):
        hm = default_hm
        hm.put('a', 1)
        index = hm._hash('a')
        assert len(hm) == 1
        assert len(hm._buckets) == 8    # this is still the max bucket capacity
        assert len(hm._buckets[index]) == 1


    def test_add_to_populated_bucket(self):
        pass


    def test_reset_existing_key(self):
        pass


'''
    def test_something_else(self):
        items = [('a', 1)]
        hm = _make_hm(items)
        print(hm._buckets)
        assert len(hm) == 1
        assert len(hm._buckets[0]) == 1
'''


class TestGet:
    def test_get_existing_value(self):
        pass


    def test_get_non_existing_value(self, default_hm):
        hm = default_hm
        assert hm.get('a') == None


    def test_get_passed_default_value(self, default_hm):
        hm = default_hm
        assert hm.get('a', 'not here') == 'not here'
