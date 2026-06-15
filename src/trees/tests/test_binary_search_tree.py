import pytest
from ..binary_search_tree import BSTNode, BinarySearchTree


@pytest.fixture
def bst_only_root():
    t = BinarySearchTree()
    t.root = BSTNode(10)
    t.size += 1
    return t


@pytest.fixture
def bst_depth_two():
    t = BinarySearchTree()
    t.root = BSTNode(20)
    t.root.left = BSTNode(10)
    t.root.right = BSTNode(30)
    t.size += 3
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
    def test_new_node_for_root(self):
        t = BinarySearchTree()
        n = t._insert(t.root, 1)
        n.value = 1


    def test_new_left_node(self, bst_only_root):
        t = bst_only_root
        t._insert(t.root, 9)
        assert t.root.left.value == 9
        assert t.root.right == None


    def test_new_right_node(self, bst_only_root):
        t = bst_only_root
        t._insert(t.root, 11)
        assert t.root.right.value == 11
        assert t.root.left == None


    def test_new_node_null_pointers(self, bst_only_root):
        t = bst_only_root
        t._insert(t.root, 1)
        new_node = t.root.left
        assert new_node.left == None
        assert new_node.right == None


    def test_new_node_below_root(self, bst_depth_two):
        t = bst_depth_two
        target_node = t.root.left
        t._insert(target_node, 1)
        assert target_node.left.value == 1
        assert target_node.right == None


    def test_insert_duplicate_raises(self, bst_only_root):
        t = bst_only_root
        with pytest.raises(ValueError) as e:
            t.insert(10)

        assert str(e.value) == '10 is already in this BST'


class TestInsert:
    def test_set_root(self):
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
