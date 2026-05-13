import pytest
from singly_linked_list import Node, SinglyLinkedList


@pytest.fixture
def empty_sll():
    sll = SinglyLinkedList()
    return sll


@pytest.fixture
def sample_sll():
    sll = SinglyLinkedList()
    for i in [1, 2, 3]:
        sll.append_fast(i)
    return sll


def test_node_initialization():
    n = Node(5)
    assert n.value == 5
    assert n.next is None


def test_linkedlist_initialization():
    sll = SinglyLinkedList()
    assert sll.head is None
    assert sll.length == 0
    assert sll.to_list() == []


class TestPrepend:
    def test_prepend_to_empty_list(self, empty_sll):
        empty_sll.prepend(1)
        assert empty_sll.to_list() == [1]


    def test_prepend_to_existing_list(self, sample_sll):
        sample_sll.prepend(0)
        assert sample_sll.to_list() == [0, 1, 2, 3]


    def test_prepend_negative_number(self, sample_sll):
        sample_sll.prepend(-1)
        assert sample_sll.to_list() == [-1, 1, 2, 3]


    def test_prepend_null_value(self, empty_sll):
        #TODO: This really should be guarded differently in the sll.method
        #TODO: Test with other non-integer datatypes
        with pytest.raises(TypeError):
            empty_sll.prepend()


    def test_prepend_sets_head_and_tail(self, empty_sll):
        empty_sll.prepend(1)
        assert empty_sll.head.value == 1
        assert empty_sll.tail.value == 1


    def test_prepend_advances_head_pointer(self, sample_sll):
        sample_sll.prepend(0)
        assert sample_sll.head.value == 0
        assert sample_sll.head.next.value == 1


    def test_prepend_increments_length(self, sample_sll):
        sample_sll.prepend(4)
        assert len(sample_sll) == 4


class TestAppendSlow:
    def test_append_to_empty_list(self, empty_sll):
        empty_sll.append_slow(1)
        assert empty_sll.to_list() == [1]


    def test_append_to_existing_list(self, sample_sll):
        sample_sll.append_slow(0)
        assert sample_sll.to_list() == [1, 2, 3, 0]


    def test_prepend_null_value(self, sample_sll):
        #TODO: This really should be guarded differently in the sll.method
        #TODO: Test with other non-integer datatypes
        with pytest.raises(TypeError):
            sample_sll.append_slow()


    def test_append_sets_head_and_tail(self, empty_sll):
        empty_sll.append_slow(1)
        assert empty_sll.head.value == 1
        assert empty_sll.tail.value == 1


    def test_append_advances_tail_pointer(self, sample_sll):
        sample_sll.append_slow(0)
        assert sample_sll.tail.value == 0
        assert sample_sll.tail.next is None


    def test_append_increments_length(self, sample_sll):
        sample_sll.append_slow(4)
        assert len(sample_sll) == 4


class TestAppendFast:
    def test_append_to_empty_list(self, empty_sll):
        empty_sll.append_fast(1)
        assert empty_sll.to_list() == [1]


    def test_append_to_existing_list(self, sample_sll):
        sample_sll.append_fast(0)
        assert sample_sll.to_list() == [1, 2, 3, 0]


    def test_prepend_null_value(self, sample_sll):
        #TODO: This really should be guarded differently in the sll.method
        with pytest.raises(TypeError):
            sample_sll.append_fast()


    def test_append_sets_head_and_tail(self, empty_sll):
        empty_sll.append_fast(1)
        assert empty_sll.head.value == 1
        assert empty_sll.tail.value == 1


    def test_append_advances_tail_pointer(self, sample_sll):
        sample_sll.append_fast(0)
        assert sample_sll.tail.value == 0


    def test_append_increments_length(self, sample_sll):
        sample_sll.append_fast(4)
        assert len(sample_sll) == 4


class TestDelete: 
    @pytest.mark.parametrize('values, delete, expected', [
        ([1, 2, 3, 4], 2, [1, 3, 4]),       # middle
        ([1, 2, 3, 4], 1, [2, 3, 4]),       # head
        ([1, 2, 3, 4], 4, [1, 2, 3]),       # tail
        ([1, 2, 2, 3], 2, [1, 3]),          # multiple
        ([1, 1, 2, 3], 1, [2, 3]),          # multiple at head
        ([1, 2, 3, 3], 3, [1, 2]),          # multiple at tail
        ([1, 2, 3, 2, 4], 2, [1, 3, 4]),    # multiple non-consecutive
    ])
    def test_delete(self, values, delete, expected):
        sll = SinglyLinkedList()
        for v in values:
            sll.append_fast(v)
        sll.delete(delete)
        assert sll.to_list() == expected


    def test_delete_decrements_length(self, sample_sll):
        sample_sll.delete(2)
        assert len(sample_sll) == 2


    def test_delete_head_updates_head_pointer(self):
        sll = SinglyLinkedList()
        for v in [1, 2, 3]:
            sll.append_fast(v)
        sll.delete(1)
        assert sll.head.value == 2
        assert sll.head.next.value == 3


    def test_delete_tail_updates_tail_pointer(self):
        sll = SinglyLinkedList()
        for v in [1, 2, 3]:
            sll.append_fast(v)
        sll.delete(3)
        assert sll.tail.value == 2
        assert sll.tail.next is None
        

    def test_delete_only_node_nulls_both_pointers(self):
        sll = SinglyLinkedList()
        sll.append_fast(1)
        sll.delete(1)
        assert sll.head is None
        assert sll.tail is None


class TestCount:
    @pytest.mark.parametrize('values, target, expected', [
        ([1, 2, 3], 1, 1),      # head
        ([1, 2, 3], 3, 1),      # tail
        ([1, 1, 2], 1, 2),      # sequential
        ([1, 2, 1, 3], 1, 2),   # non-sequential
        ([1, 1, 1], 1, 3),      # all
        ([1, 2, 1], 1, 2),      # head and tail
        ([1, 2, 3], 4, 0),      # none
    ])
    def test_count(self, values, target, expected):
        sll = SinglyLinkedList()
        for v in values:
            sll.append_fast(v)
        assert sll.count(target) == expected


class TestSearch:
    @pytest.mark.parametrize('values, target, expected', [
        ([1, 2, 3], 1, [0]),            # head
        ([1, 2, 3], 3, [2]),            # tail
        ([1, 1, 2], 1, [0, 1]),         # sequential
        ([1, 2, 1, 3], 1, [0, 2]),      # non-sequential
        ([1, 1, 1], 1, [0, 1, 2]),      # all
        ([1, 2, 1], 1, [0, 2]),         # head and tail
        ([1, 2, 3], 4, []),             # none
    ])
    def test_search(self, values, target, expected):
        sll = SinglyLinkedList()
        for v in values:
            sll.append_fast(v)
        assert sll.search(target) == expected


class ComponentTest:
    def test_component(self):
        sll = SinglyLinkedList()
        sll.append_fast(1)
        sll.append_slow(2)
        sll.prepend(3)
        sll.delete(2)
        sll.prepend(2)
        assert sll.to_list() == [2, 3, 1]
        assert sll.head.value == 2
        assert sll.head.value.next == 3
        assert sll.tail.value == 1
        assert len(sll) == 3
