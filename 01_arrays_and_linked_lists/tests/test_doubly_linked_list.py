import pytest
from doubly_linked_list import Node, DoublyLinkedList


def test_node():
    n = Node(5)
    assert n.previous == None
    assert n.next == None
    assert n.get_value() == 5


def test_initialization():
    dll = DoublyLinkedList()
    assert dll.head is None
    assert dll.tail is None
    assert dll.length == 0



# --- component tests --- #
@pytest.mark.parametrize('values, expected', [
    ([10], [10]),
    ([1, 2, 3], [1, 2, 3]),
    (['first', 'second', 'third'], ['first', 'second', 'third']), 
    ([], []),
])
def test_append_various(values, expected):
    dll = DoublyLinkedList()
    for v in values:
        dll.append(v)
    assert dll.to_list() == expected


@pytest.mark.parametrize('values, expected', [
    ([10], [10]),
    ([1, 2, 3], [3, 2, 1]),
    (['first', 'second', 'third'], ['third', 'second', 'first']),
    ([], []),
])
def test_prepend_various(values, expected):
    dll = DoublyLinkedList()
    for v in values:
        dll.prepend(v)
    assert dll.to_list() == expected


@pytest.mark.parametrize('values, delete, expected', [
    ([1, 2, 3, 4, 5], 2, [1, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 1, [2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4]),
    ([1], 1, []),
    ([], None, []),
    ([], 1, []),
    ([1], 2, [1]),
])
def test_delete_first(values, delete, expected):
    dll = DoublyLinkedList()
    for v in values:
        dll.append(v)
    dll.delete_first(delete)
    assert dll.to_list() == expected


@pytest.mark.parametrize('values, delete, expected', [
    ([1, 2, 3, 4, 5], 2, [1, 3, 4, 5]),
    ([1, 2, 3, 2, 5], 2, [1, 2, 3, 5]),
    ([1], 1, []),
    ([1, 1], 1, [1]),
    ([2, 1], 1, [2]),
])
def test_delete_first_from_end(values, delete, expected):
    dll = DoublyLinkedList()
    for v in values:
        dll.append(v)
    dll.delete_first(delete, from_end=True)
    assert dll.to_list() == expected


@pytest.mark.parametrize('values, delete, expected', [
    ([1, 2, 3, 4, 5], 2, [1, 3, 4, 5]),
    ([1, 2, 3, 2, 5], 2, [1, 3, 5]),
    ([1, 2, 3, 4, 5], 1, [2, 3, 4, 5]),
    ([1, 1, 2, 3, 4], 1, [2, 3, 4]),
    ([1, 2, 3, 3, 4], 3, [1, 2, 4]),
    ([1, 2, 3, 4, 4], 4, [1, 2, 3]),
    ([1, 2, 3, 4, 1], 1, [2, 3, 4]),
    ([1, 1], 1, []),
    ([], None, []),
])
def test_delete_all(values, delete, expected):
    dll = DoublyLinkedList()
    for v in values:
        dll.append(v)
    dll.delete_all(delete)
    assert dll.to_list() == expected

# --- setup --- #
@pytest.fixture
def sample_dll():
    dll = DoublyLinkedList()
    for i in [10, 20, 30, 40]:
        dll.append(i)
    return dll


# --- integration tests --- #
def test_head_movement(sample_dll):
    assert sample_dll.head.get_value() == 10
    sample_dll.prepend(1)
    assert sample_dll.head.get_value() == 1


def test_tail_movement(sample_dll):
    assert sample_dll.tail.get_value() == 40
    sample_dll.append(1)
    assert sample_dll.tail.get_value() == 1


def test_length_tracking(sample_dll):
    assert sample_dll.get_length() == 4
    sample_dll.append(50)
    assert sample_dll.get_length() == 5
    sample_dll.prepend(10)
    assert sample_dll.get_length() == 6
    sample_dll.delete_first(20)
    assert sample_dll.get_length() == 5
    sample_dll.delete_all(10)
    assert sample_dll.get_length() == 3
