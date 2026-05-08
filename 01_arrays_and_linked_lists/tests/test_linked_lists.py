import pytest
from linked_list import Node, LinkedList


def test_node():
    n = Node(5)
    assert n.next == None
    assert n.get_value() == 5


def test_initialization():
    ll = LinkedList()
    assert ll.head is None
    assert ll.length == 0
    assert ll.to_list() == []


# --- setup --- #
@pytest.fixture
def sample_ll():
    ll = LinkedList()
    for i in [10, 20, 30, 40]:
        ll.append_fast(i)
    return ll


# --- component tests --- #
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


@pytest.mark.parametrize('values, delete, expected', [
    ([10, 20, 30, 40], 20, [10, 30, 40]),
    ([10, 20, 30, 40], 10, [20, 30, 40]),
    ([10, 20, 30, 40], 40, [10, 20, 30]),
    ([10, 20, 20, 30], 20, [10, 30]),
    ([10, 10, 20, 30], 10, [20, 30]),
    ([10, 20, 30, 30], 30, [10, 20]),
    ([10, 20, 30, 20, 40], 20, [10, 30, 40]),
])
def test_delete_various(values, delete, expected):
    ll = LinkedList()
    for v in values:
        ll.append_fast(v)
    ll.delete(delete)
    assert ll.to_list() == expected
   

# --- integration tests --- #
def test_integration():
    ll = LinkedList()
    assert ll.get_length() == 0
    ll.append_slow(2)
    ll.head.get_value() == 2
    ll.tail.get_value() == 2
    ll.prepend(1)
    ll.head.get_value() == 1
    ll.tail.get_value() == 2
    for v in [3, 4, 5]:
        ll.append_fast(v)
    assert ll.get_length() == 5
    assert ll.to_list() == [1, 2, 3, 4, 5]
    assert ll.head.get_value() == 1
    assert ll.tail.get_value() == 5
