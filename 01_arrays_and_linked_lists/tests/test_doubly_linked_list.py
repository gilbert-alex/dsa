import pytest
from doubly_linked_list import Node, DoublyLinkedList


def test_node():
    n = Node(5)
    assert n.previous == None
    assert n.next == None
    assert n.get_value() == 5


@pytest.fixture
def empty_dll():
    return DoublyLinkedList()


@pytest.fixture
def sample_dll():
    dll = DoublyLinkedList()
    for i in [10, 20, 30, 40]:
        dll.append(i)
    return dll


@pytest.fixture
def sample_dll_with_duplicates():
    dll = LinkedList()
    for i in [10, 10, 10, 20, 30, 30]:
        dll.append(i)
    return dll


def test_initialization():
    dll = DoublyLinkedList()
    assert dll.head is None
    assert dll.tail is None
    assert dll.length == 0


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


def test_length(sample_dll):
    assert sample_dll.get_length() == 4
    sample_dll.append(50)
    assert sample_dll.get_length() == 5


def test_head(sample_dll):
    assert sample_dll.head.get_value() == 10
    sample_dll.prepend(1)
    assert sample_dll.head.get_value() == 1


def test_tail(sample_dll):
    assert sample_dll.tail.get_value() == 40
    sample_dll.append(1)
    assert sample_dll.tail.get_value() == 1
