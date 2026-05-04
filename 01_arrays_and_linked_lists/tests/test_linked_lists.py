import pytest

from linked_list import LinkedList


@pytest.fixture
def empty_ll():
    return LinkedList()


@pytest.fixture
def sample_ll():
    ll = LinkedList()
    for i in [10, 20, 30, 40]:
        ll.prepend(i)
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
def test_prepends(values, expected):
    ll = LinkedList()
    for v in values:
        ll.prepend(v)
    assert ll.to_list() == expected


def test_sample_ll(sample_ll):
    assert sample_ll.to_list() == [40, 30, 20, 10]


def test_delete(sample_ll):
    sample_ll.delete(20)
    assert sample_ll.to_list() == [40, 30, 10]
