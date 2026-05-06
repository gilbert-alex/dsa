import pytest
from linked_list import LinkedList


@pytest.fixture
def empty_ll():
    return LinkedList()


@pytest.fixture
def sample_ll():
    ll = LinkedList()
    for i in [10, 20, 30, 40]:
        ll.append_slow(i)
    return ll


@pytest.fixture
def sample_ll_with_duplicates():
    ll = LinkedList()
    for i in [10, 10, 10, 20, 30, 30]:
        ll.append_slow(i)
    return ll


def test_initialization(empty_ll):
    assert empty_ll.head is None
    assert empty_ll.length == 0
    assert empty_ll.to_list() == []


@pytest.mark.parametrize('values, expected', [
    ([10], [10]),
    ([1, 2, 3], [3, 2, 1]),
    ([], []),
])
def test_prepend(values, expected):
    ll = LinkedList()
    for v in values:
        ll.prepend(v)
    assert ll.to_list() == expected


@pytest.mark.parametrize('values, expected', [
    ([10], [10]),
    ([1, 2, 3], [1, 2, 3]),
    ([], []),
])
def test_append_slow(values, expected):
    ll = LinkedList()
    for v in values:
        ll.append_slow(v)
    assert ll.to_list() == expected


'''
@pytest.mark.parametrize('values, expected', [
    ([10], [10]),
    ([1, 2, 3], [1, 2, 3]),
    ([], []),
])
def test_append_fast(values, expected):
    ll = LinkedList()
    for v in values:
        ll.append_fast(v)
    assert ll.to_list() == expected
'''


def test_delete(sample_ll):
    sample_ll.delete(20)
    assert sample_ll.to_list() == [10, 30, 40]
    assert sample_ll.get_length() == 3
    for i in sample_ll.to_list():
        #print(f'deleting {i}')  #debug
        sample_ll.delete(i)
    assert sample_ll.to_list() == []
    assert sample_ll.get_length() == 0


def test_delete_first_element(sample_ll):
    sample_ll.delete(40)
    assert sample_ll.to_list() == [10, 20, 30]


def test_delete_last_element(sample_ll):
    sample_ll.delete(10)
    assert sample_ll.to_list() == [20, 30, 40]


def test_search(sample_ll_with_duplicates):
    assert sample_ll_with_duplicates.search(10) == 3
