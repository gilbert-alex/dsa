import pytest
from ..stack import LinkedListStack


@pytest.fixture
def empty_ls():
    return LinkedListStack()


@pytest.fixture
def sample_ls():
    return _make_ls(1, 2, 3)


def _make_ls(*values):
    ls = LinkedListStack()
    for v in values:
        ls._data.prepend(v)
    return ls


def test_initialization():
    ls = LinkedListStack()
    assert len(ls) == 0
    assert ls.is_empty()
    with pytest.raises(IndexError):
        ls.peek()
    with pytest.raises(IndexError):
        ls.pop()
    

class TestPush():
    def test_push_to_empty_stack(self, empty_ls):
        empty_ls.push(1)
        assert empty_ls.peek() == 1
        assert empty_ls.is_empty() == False
        assert len(empty_ls) == 1


    def test_push_to_existing_stack(self, sample_ls):
        sample_ls.push(4)
        assert sample_ls.peek() == 4
        assert sample_ls.is_empty() == False
        assert len(sample_ls) == 4
    

    def test_push_increments_length(self, sample_ls):
        before = len(sample_ls)
        sample_ls.push(4)
        after = len(sample_ls)
        assert after == before + 1

    
class TestPop():
    @pytest.mark.parametrize('values, new_top, new_len, popped', [
        ([1, 2, 3], 2, 2, 3),                   # ascending
        ([1, 2, 2], 2, 2, 2),                   # duplicate
        ([4, 3, 2], 3, 2, 2),                   # decending
        ([-1, -2, -3], -2, 2, -3),              # negative
        ([2, 1, 0], 1, 2, 0),                   # zero/falsy
        (['a', 'b', 'c'], 'b', 2, 'c'),         # string
    ])
    def test_pop_removes_top_value(self, values, new_top, new_len, popped):
        ls = _make_ls(*values)
        p = ls.pop()
        assert p == popped
        assert ls.peek() == new_top
        assert len(ls) == new_len


    def test_pop_returns_value(self, sample_ls):
        popped = sample_ls.pop()
        assert popped == 3


    def test_pop_decrements_length(self, sample_ls):
        before = len(sample_ls)
        sample_ls.pop()
        after = len(sample_ls)
        assert after == before - 1


    def test_pop_from_empty_raises_error(self, empty_ls):
        with pytest.raises(IndexError):
            empty_ls.pop()


class TestPeek():
    def test_peek_returns_value(self, sample_ls):
        assert sample_ls.peek() == 3


    def test_peek_does_not_mutate_stack(self, sample_ls):
        before_string = repr(sample_ls)
        for _ in range(2):
            sample_ls.peek()
        after_string = repr(sample_ls)
        assert before_string == after_string


    def test_peek_from_empty_raises_error(self, empty_ls):
        with pytest.raises(IndexError):
            empty_ls.peek()
