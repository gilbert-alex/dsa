import pytest
from ..stack import ListStack


@pytest.fixture
def empty_ls():
    return ListStack()


@pytest.fixture
def sample_ls():
    ls = ListStack()
    for i in [1, 2, 3]:
        ls.push(i)
    return ls 


def _make_ls(*values):
    ls = ListStack()
    ls._data = list(values)
    return ls


def test_initialization():
    ls = ListStack()
    assert len(ls) == 0
    assert ls.is_empty()
    with pytest.raises(IndexError):
        ls.peek()
    with pytest.raises(IndexError):
        ls.pop()
    

class TestPush():
    def test_push_to_empty_stack(self, empty_ls):
        empty_ls.push(1)
        assert empty_ls._data == [1]


    def test_push_to_existing_stack(self, sample_ls):
        sample_ls.push(4)
        assert sample_ls._data == [1, 2, 3, 4]
    
    
class TestPop():
    @pytest.mark.parametrize('values, expected', [
        ([1, 2, 3, 4], [1, 2, 3]),           # ascending
        ([1, 2, 3, 3], [1, 2, 3]),           # duplicate
        ([4, 3, 2, 1], [4, 3, 2]),           # decending
        ([1, 2, 3, -1], [1, 2, 3]),          # negative
        ([1, 2, 3, 'four'], [1, 2, 3]),      # string
    ])
    def test_pop(self, values, expected):
        ls = _make_ls(*values)
        ls.pop()
        assert ls._data == expected


    def test_pop_from_stack(self, sample_ls):
        popped = sample_ls.pop()
        assert popped == 3
        assert sample_ls._data == [1, 2]


    def test_pop_from_empty_stack(self, empty_ls):
        with pytest.raises(IndexError):
            empty_ls.pop()
