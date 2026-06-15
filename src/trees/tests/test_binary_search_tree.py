import pytest
from ..binary_search_tree import BSTNode, BinarySearchTree


@pytest.fixture
def bst_only_root():
    t = BinarySearchTree()
    t.root = BSTNode(10)
    t.size += 1
    return t


class TestSetup:
    def test_bst_only_root(self, bst_only_root):
        assert bst_only_root.root.value == 10
        assert bst_only_root.root.left == None
        assert bst_only_root.root.right == None
        assert len(bst_only_root) == 1


class TestBSTNode:
    def test_init(self):
        n = BSTNode(5)
        assert n.value == 5
        assert n.left == None
        assert n.right == None


class TestBinarySearchTree:
    def test_init(self):
        t = BinarySearchTree()
        assert t.root == None
        assert len(t) == 0


    def test_component(self):
        #TODO: do this when core BST methods are in place
        pass


class TestInsertPrivate:
    def test_create_new_root(self):
        t = BinarySearchTree()
        assert t.root == None
        t.insert(1)
        assert t.root != None
        assert t.root.value == 1


    def test_new_left_node(self, bst_only_root):
        t = bst_only_root
        t.insert(9)
        assert t.root.left.value == 9


    def test_new_right_node(self, bst_only_root):
        t = bst_only_root
        t.insert(11)
        assert t.root.right.value == 11


    def test_new_node_child_pointers(self, bst_only_root):
        t = bst_only_root
        t.insert(1)
        new_node = t.root.left
        assert new_node.left == None
        assert new_node.right == None


    def test_insert_duplicate_raises(self, bst_only_root):
        t = bst_only_root
        with pytest.raises(ValueError) as e:
            t.insert(10)

        assert str(e.value) == '10 is already in this BST'


class TestInsert:
    def test_create_new_bst(self):
        t = BinarySearchTree()
        assert t.root == None
        t.insert(1)
        assert t.root.value == 1


    def test_insert_increments_size(self):
        t = BinarySearchTree()
        assert len(t) == 0
        t.insert(1)
        assert len(t) == 1


    def test_insert_duplicate_raises(self):
        t = BinarySearchTree()
        t.insert(2)
        with pytest.raises(ValueError) as e:
            t.insert(2)

        assert str(e.value) == '2 is already in this BST'
