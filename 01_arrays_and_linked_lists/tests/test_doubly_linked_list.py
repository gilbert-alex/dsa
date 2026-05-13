import pytest
from doubly_linked_list import Node, DoublyLinkedList


@pytest.fixture
def empty_dll():
    dll = DoublyLinkedList()
    return dll


@pytest.fixture
def sample_dll():
    dll = DoublyLinkedList()
    for i in [1, 2, 3]:
        dll.append(i)
    return dll


def test_node_initialization():
    n = Node(5)
    assert n.value == 5
    assert n.previous is None
    assert n.next is None


def test_initialization():
    dll = DoublyLinkedList()
    assert dll.head is None
    assert dll.tail is None
    assert dll.length == 0
    assert dll.to_list() == []


class TestPrepend:
    def test_prepend_to_empty_list(self, empty_dll):
        empty_dll.prepend(1)
        assert empty_dll.to_list() == [1]
        

    def test_prepend_to_existing_list(self, sample_dll):
        sample_dll.prepend(0)
        assert sample_dll.to_list() == [0, 1, 2, 3]


    def test_prepend_negative_number(self, sample_dll):
        sample_dll.prepend(-1)
        assert sample_dll.to_list() == [-1, 1, 2, 3]


    def test_prepend_null_value(self, empty_dll):
        #TODO: This really should be guarded differently in the dll.method
        #TODO: Test with other non-integer datatypes
        with pytest.raises(TypeError):
            empty_dll.prepend()


    def test_prepend_sets_head_and_tail(self, empty_dll):
        empty_dll.prepend(1)
        assert empty_dll.head.value == 1
        assert empty_dll.tail.value == 1


    def test_prepend_advances_head_pointer(self, sample_dll):
        sample_dll.prepend(0)
        assert sample_dll.head.value == 0
        assert sample_dll.head.next.value == 1
        assert sample_dll.head.previous is None


    def test_prepend_increments_length(self, sample_dll):
        sample_dll.prepend(0)
        assert len(sample_dll) == 4


class TestAppend:
    def test_append_to_empty_list(self, empty_dll):
        empty_dll.append(1)
        assert empty_dll.to_list() == [1]


    def test_append_to_existing_list(self, sample_dll):
        sample_dll.append(0)
        assert sample_dll.to_list() == [1, 2, 3, 0]


    def test_prepend_null_value(self, sample_dll):
        #TODO: This really should be guarded differently in the dll.method
        #TODO: Test with other non-integer types
        with pytest.raises(TypeError):
            sample_dll.append()


    def test_append_sets_head_and_tail(self, empty_dll):
        empty_dll.append(1)
        assert empty_dll.head.value == 1
        assert empty_dll.tail.value == 1


    def test_append_advances_tail_pointer(self, sample_dll):
        sample_dll.append(4)
        assert sample_dll.tail.value == 4
        assert sample_dll.tail.previous.value == 3
        assert sample_dll.tail.next is None


    def test_append_increments_length(self, sample_dll):
        sample_dll.append(4)
        assert len(sample_dll) == 4


class TestDeleteFirst:
    @pytest.mark.parametrize('values, delete, expected', [
        ([1, 2, 3, 4], 2, [1, 3, 4]),           # middle
        ([1, 2, 3, 4], 1, [2, 3, 4]),           # head
        ([1, 2, 3, 4], 4, [1, 2, 3]),           # tail
        ([1, 2, 2, 3], 2, [1, 2, 3]),           # multiple
        ([1, 1, 2, 3], 1, [1, 2, 3]),           # multiple at head
        ([1, 2, 3, 3], 3, [1, 2, 3]),           # multiple at tail
        ([1, 2, 3, 2, 4], 2, [1, 3, 2, 4]),     # multiple non-consecutive
    ])
    def test_delete_first(self, values, delete, expected):
        dll = DoublyLinkedList()
        for v in values:
            dll.append(v)
        dll.delete_first(delete)
        assert dll.to_list() == expected


    @pytest.mark.parametrize('values, delete, expected', [
        ([1, 2, 3, 4], 2, [1, 3, 4]),           # middle
        ([1, 2, 3, 4], 1, [2, 3, 4]),           # head
        ([1, 2, 3, 4], 4, [1, 2, 3]),           # tail
        ([1, 2, 2, 3], 2, [1, 2, 3]),           # multiple
        ([1, 1, 2, 3], 1, [1, 2, 3]),           # multiple at head
        ([1, 2, 3, 3], 3, [1, 2, 3]),           # multiple at tail
        ([1, 2, 3, 2, 4], 2, [1, 2, 3, 4]),     # multiple non-consecutive
    ])
    def test_delete_first_from_end(self, values, delete, expected):
        dll = DoublyLinkedList()
        for v in values:
            dll.append(v)
        dll.delete_first(delete, from_end=True)
        assert dll.to_list() == expected


    def test_delete_decrements_length(self, sample_dll):
        sample_dll.delete_first(2)
        assert len(sample_dll) == 2


    def test_delete_head_updates_head_pointer(self):
        dll = DoublyLinkedList()
        for v in [1, 2, 3]:
            dll.append(v)
        dll.delete_first(1)
        assert dll.head.value == 2
        assert dll.head.previous is None
        assert dll.head.next.value == 3


    def test_delete_tail_updates_tail_pointer(self):
        dll = DoublyLinkedList()
        for v in [1, 2, 3]:
            dll.append(v)
        dll.delete_first(3)
        assert len(dll) == 2
        assert dll.tail.value == 2
        assert dll.tail.previous.value == 1
        assert dll.tail.next is None


    def test_delete_only_node_nulls_both_pointers(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.delete_first(1)
        assert dll.head is None
        assert dll.tail is None


    def test_delete_raises_not_found(self, sample_dll):
        with pytest.raises(ValueError):
            sample_dll.delete_first(4)


class TestDeleteAll:
    @pytest.mark.parametrize('values, delete, expected', [
        ([1, 2, 3, 4, 5], 2, [1, 3, 4, 5]),     # single
        ([1, 2, 3, 2, 5], 2, [1, 3, 5]),        # multiple non-consecutive
        ([1, 2, 3, 4, 5], 1, [2, 3, 4, 5]),     # head
        ([1, 1, 2, 3, 4], 1, [2, 3, 4]),        # mutliple at head
        ([1, 2, 3, 3, 4], 3, [1, 2, 4]),        # multiple consecutive
        ([1, 2, 3, 4, 4], 4, [1, 2, 3]),        # multiple at tail
        ([1, 2, 3, 4, 1], 1, [2, 3, 4]),        # head and tail
        ([1, 1], 1, []),                        # all
    ])
    def test_delete_all(self, values, delete, expected):
        dll = DoublyLinkedList()
        for v in values:
            dll.append(v)
        dll.delete_all(delete)
        assert dll.to_list() == expected


    def test_delete_decrements_length(self, sample_dll):
        sample_dll.delete_all(2)
        assert len(sample_dll) == 2


    def test_delete_head_updates_head_pointer(self):
        dll = DoublyLinkedList()
        for v in [1, 2, 3]:
            dll.append(v)
        dll.delete_all(1)
        assert dll.head.value == 2
        assert dll.head.previous is None
        assert dll.head.next.value == 3


    def test_delete_tail_updates_tail_pointer(self):
        dll = DoublyLinkedList()
        for v in [1, 2, 3]:
            dll.append(v)
        dll.delete_all(3)
        assert len(dll) == 2
        assert dll.tail.value == 2
        assert dll.tail.previous.value == 1
        assert dll.tail.next is None


    def test_delete_only_node_nulls_both_pointers(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.delete_all(1)
        assert dll.head is None
        assert dll.tail is None

'''
    # this is not implemented yet on the method
    def test_delete_raises_not_found(self, sample_dll):
        with pytest.raises(ValueError):
            sample_dll.delete_all(4)
'''

class ComponentTest:
    def test_component():
        dll = DoublyLinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.get_length() == 0

        dll.append(2)
        assert dll.head.value == 2
        assert dll.tail.value == 2

        dll.prepend(1)
        assert dll.head.value == 1
        assert dll.tail.value == 2

        for v in [3, 4, 5]:
            dll.append(v)
        assert dll.get_length() == 5
        assert dll.to_list() == [1, 2, 3, 4, 5]
        assert dll.head.value == 1
        assert dll.tail.value == 5
        
        dll.delete_first(1)
        assert dll.get_length() == 4
        assert dll.to_list() == [2, 3, 4, 5]
        assert dll.head.value == 2
        assert dll.tail.value == 5

        dll.delete_first(5)
        assert dll.get_length() == 3
        assert dll.to_list() == [2, 3, 4]
        assert dll.head.value == 2
        assert dll.tail.value == 4

        for v in dll.to_list():
            dll.delete_first(v)
        assert dll.get_length() == 0
        assert dll.to_list() == []
        assert dll.head == None
        assert dll.tail == None
        
        for v in [2, 3, 2]:
            dll.append(v)
        dll.delete_first(2, from_end=True)
        assert dll.to_list() == [2, 3]
        assert dll.head.value == 2
        assert dll.tail.value == 3
        
        dll.append(3)
        dll.delete_all(3)
        assert dll.to_list() == [2]
        assert dll.get_length() == 1
        assert dll.head.value == 2
        assert dll.head.value == 2
