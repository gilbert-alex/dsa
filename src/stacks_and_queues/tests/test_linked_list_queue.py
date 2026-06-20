import pytest
from ..queue import LinkedListQueue


@pytest.fixture
def empty_llq():
    return LinkedListQueue()


@pytest.fixture
def sample_llq():
    return _make_llq(1, 2, 3)


def _make_llq(*items):
    llq = LinkedListQueue()
    for v in items:
        llq._data.append_fast(v)
    return llq


def test_initialization():
    llq = LinkedListQueue()
    assert len(llq) == 0
    assert llq.is_empty()
    with pytest.raises(IndexError):
        llq.peek()
    with pytest.raises(IndexError):
        llq.dequeue()
    

class TestWhileCondition:
    def test_false(self):
        llq = LinkedListQueue()
        result = bool(llq)
        assert result == False


    def test_true(self):
        llq = LinkedListQueue()
        llq.enqueue(1)
        result = bool(llq)
        assert result == True


class TestEnqueue():
    def test_enqueue_to_empty_stack(self, empty_llq):
        empty_llq.enqueue(1)
        assert empty_llq.peek() == 1
        assert empty_llq.is_empty() == False
        assert len(empty_llq) == 1


    def test_enqueue_to_existing_stack(self, sample_llq):
        sample_llq.enqueue(4)
        assert sample_llq.peek() == 1
        assert sample_llq.is_empty() == False
        assert len(sample_llq) == 4
    

    def test_enqueue_increments_length(self, sample_llq):
        before = len(sample_llq)
        sample_llq.enqueue(4)
        after = len(sample_llq)
        assert after == before + 1

    
class TestDequeue():
    @pytest.mark.parametrize('items, new_top, new_len, dequeued', [
        ([1, 2, 3], 2, 2, 1),                   # ascending
        ([2, 2, 2], 2, 2, 2),                   # duplicate
        ([4, 3, 2], 3, 2, 4),                   # decending
        ([-1, -2, -3], -2, 2, -1),              # negative
        ([2, 1, 0], 1, 2, 2),                   # zero/falsy
        (['a', 'b', 'c'], 'b', 2, 'a'),         # string
    ])
    def test_dequeue_removes_top_item(self, items, new_top, new_len, dequeued):
        llq = _make_llq(*items)
        d = llq.dequeue()
        assert d == dequeued
        assert llq.peek() == new_top
        assert len(llq) == new_len


    def test_dequeue_returns_item(self, sample_llq):
        dequeued = sample_llq.dequeue()
        assert dequeued == 1


    def test_dequeue_decrements_length(self, sample_llq):
        before = len(sample_llq)
        sample_llq.dequeue()
        after = len(sample_llq)
        assert after == before - 1


    def test_dequeue_from_empty_raises_error(self, empty_llq):
        with pytest.raises(IndexError):
            empty_llq.dequeue()


class TestPeek():
    def test_peek_returns_item(self, sample_llq):
        assert sample_llq.peek() == 1


    def test_peek_does_not_mutate_stack(self, sample_llq):
        before_string = repr(sample_llq)
        for _ in range(2):
            sample_llq.peek()
        after_string = repr(sample_llq)
        assert before_string == after_string


    def test_peek_from_empty_raises_error(self, empty_llq):
        with pytest.raises(IndexError):
            empty_llq.peek()
