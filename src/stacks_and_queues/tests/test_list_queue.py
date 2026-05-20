import pytest
from ..queue import ListQueue


@pytest.fixture
def empty_lq():
    return ListQueue()


@pytest.fixture
def sample_lq():
    return _make_lq(1, 2, 3)


def _make_lq(*items):
    lq = ListQueue()
    lq._data = list(items)
    return lq


def test_initialization():
    lq = ListQueue()
    assert len(lq) == 0
    assert lq.is_empty()
    with pytest.raises(IndexError):
        lq.peek()
    with pytest.raises(IndexError):
        lq.dequeue()
    

class TestEnqueue():
    def test_enqueue_to_empty_queue(self, empty_lq):
        empty_lq.enqueue(1)
        assert empty_lq.peek() == 1
        assert empty_lq.is_empty() == False
        assert len(empty_lq) == 1


    def test_enqueue_to_existing_queue(self, sample_lq):
        sample_lq.enqueue(4)
        assert sample_lq.peek() == 1
        assert sample_lq.is_empty() == False
        assert len(sample_lq) == 4
    

    def test_enqueue_increments_length(self, sample_lq):
        before = len(sample_lq)
        sample_lq.enqueue(4)
        after = len(sample_lq)
        assert after == before + 1

    
class TestDequeue():
    @pytest.mark.parametrize('items, new_front, new_len, dequeued', [
        ([1, 2, 3], 2, 2, 1),                   # ascending
        ([2, 2, 2], 2, 2, 2),                   # duplicate
        ([4, 3, 2], 3, 2, 4),                   # decending
        ([-1, -2, -3], -2, 2, -1),              # negative
        ([0, 1, 2], 1, 2, 0),                   # zero/falsy
        (['a', 'b', 'c'], 'b', 2, 'a'),         # string
    ])
    def test_dequeue_removes_expected_item(self, items, new_front, new_len, dequeued):
        lq = _make_lq(*items)
        d = lq.dequeue()
        assert d == dequeued
        assert lq.peek() == new_front
        assert len(lq) == new_len


    def test_dequeue_returns_item(self, sample_lq):
        dequeued = sample_lq.dequeue()
        assert dequeued == 1


    def test_dequeue_decrements_length(self, sample_lq):
        before = len(sample_lq)
        sample_lq.dequeue()
        after = len(sample_lq)
        assert after == before - 1


    def test_dequeue_from_empty_raises_error(self, empty_lq):
        with pytest.raises(IndexError):
            empty_lq.dequeue()


class TestPeek():
    def test_peek_returns_item(self, sample_lq):
        assert sample_lq.peek() == 1


    def test_peek_does_not_mutate_queue(self, sample_lq):
        before_string = repr(sample_lq)
        for _ in range(2):
            sample_lq.peek()
        after_string = repr(sample_lq)
        assert before_string == after_string


    def test_peek_from_empty_raises_error(self, empty_lq):
        with pytest.raises(IndexError):
            empty_lq.peek()
