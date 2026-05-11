import pytest
from linked_list import Node, LinkedList


@pytest.fixture
def empty_ll():
    ll = LinkedList()
    return ll

@pytest.fixture
def sample_ll():
    ll = LinkedList()
    for i in [1, 2, 3]:
        ll.append_fast(i)
    return ll


def test_node_initialization():
    n = Node(5)
    assert n.value == 5
    assert n.next == None


def test_linkedlist_initialization():
    ll = LinkedList()
    assert ll.head is None
    assert ll.length == 0
    assert ll.to_list() == []


class TestPrepend:
    def test_prepend_to_empty_list(self, empty_ll):
        empty_ll.prepend(1)
        assert empty_ll.to_list() == [1]


    def test_prepend_to_existing_list(self, sample_ll):
        sample_ll.prepend(0)
        assert sample_ll.to_list() == [0, 1, 2, 3]


    def test_prepend_negative_number(self, sample_ll):
        sample_ll.prepend(-1)
        assert sample_ll.to_list() == [-1, 1, 2, 3]


    def test_prepend_null_value(self, empty_ll):
        #TODO: This really should be guarded differently in the ll.method
        with pytest.raises(TypeError):
            empty_ll.prepend()


    def test_prepend_sets_head_and_tail(self, empty_ll):
        empty_ll.prepend(1)
        assert empty_ll.head.get_value() == 1
        assert empty_ll.tail.get_value() == 1

    def test_prepend_advances_head_pointer(self, sample_ll):
        sample_ll.prepend(0)
        assert sample_ll.head.get_value() == 0
        assert sample_ll.head.next.get_value() == 1


    def test_prepend_increments_length(self, sample_ll):
        sample_ll.prepend(4)
        assert len(sample_ll) == 4


class TestAppendSlow:
    def test_append_to_empty_list(self, empty_ll):
        empty_ll.append_slow(1)
        assert empty_ll.to_list() == [1]


    def test_append_to_existing_list(self, sample_ll):
        sample_ll.append_slow(0)
        assert sample_ll.to_list() == [1, 2, 3, 0]


    def test_prepend_null_value(self, sample_ll):
        #TODO: This really should be guarded differently in the ll.method
        with pytest.raises(TypeError):
            sample_ll.append_slow()


    def test_append_sets_head_and_tail(self, empty_ll):
        empty_ll.append_slow(1)
        assert empty_ll.head.get_value() == 1
        assert empty_ll.tail.get_value() == 1


    def test_append_advances_tail_pointer(self, sample_ll):
        sample_ll.append_slow(0)
        assert sample_ll.tail.get_value() == 0


    def test_append_increments_length(self, sample_ll):
        sample_ll.append_slow(4)
        assert len(sample_ll) == 4


class TestAppendFast:
    def test_append_to_empty_list(self, empty_ll):
        empty_ll.append_fast(1)
        assert empty_ll.to_list() == [1]


    def test_append_to_existing_list(self, sample_ll):
        sample_ll.append_fast(0)
        assert sample_ll.to_list() == [1, 2, 3, 0]


    def test_prepend_null_value(self, sample_ll):
        #TODO: This really should be guarded differently in the ll.method
        with pytest.raises(TypeError):
            sample_ll.append_fast()


    def test_append_sets_head_and_tail(self, empty_ll):
        empty_ll.append_fast(1)
        assert empty_ll.head.get_value() == 1
        assert empty_ll.tail.get_value() == 1


    def test_append_advances_tail_pointer(self, sample_ll):
        sample_ll.append_fast(0)
        assert sample_ll.tail.get_value() == 0


    def test_append_increments_length(self, sample_ll):
        sample_ll.append_fast(4)
        assert len(sample_ll) == 4


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
        ll = LinkedList()
        for v in values:
            ll.append_fast(v)
        ll.delete(delete)
        assert ll.to_list() == expected


    def test_delete_decrements_length(self, sample_ll):
        sample_ll.delete(2)
        assert len(sample_ll) == 2


    def test_delete_head_updates_head_pointer(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append_fast(v)
        ll.delete(1)
        assert ll.head.value == 2
        assert ll.head.next.get_value() == 3


    def test_delete_tail_updates_tail_pointer(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append_fast(v)
        ll.delete(3)
        assert ll.tail.value == 2
        assert ll.tail.next is None
        

    def test_delete_only_node_nulls_both_pointers(self):
        ll = LinkedList()
        ll.append_fast(1)
        ll.delete(1)
        assert ll.head is None
        assert ll.tail is None


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
        ll = LinkedList()
        for v in values:
            ll.append_fast(v)
        assert ll.count(target) == expected


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
        ll = LinkedList()
        for v in values:
            ll.append_fast(v)
        assert ll.search(target) == expected


class ComponentTest:
    def test_component(self):
        ll = LinkedList()
        ll.append_fast(1)
        ll.append_slow(2)
        ll.prepend(3)
        ll.delete(2)
        ll.prepend(2)
        assert ll.to_list() == [2, 3, 1]
        assert ll.head.value == 2
        assert ll.head.value.next == 3
        assert ll.tail.value == 1
        assert len(ll) == 3
