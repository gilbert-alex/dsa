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


@pytest.fixture
def bst_depth_three(bst_depth_two):
    t = bst_depth_two
    left_child = t.root.left
    left_child.left = BSTNode(5)
    left_child.right = BSTNode(15)
    right_child = t.root.right
    right_child.left = BSTNode(25)
    right_child.right = BSTNode(35)
    t.size += 4
    return t


class TestSetup:
    def test_bst_only_root(self, bst_only_root):
        assert bst_only_root.root.value == 10
        assert bst_only_root.root.left == None
        assert bst_only_root.root.right == None
        assert len(bst_only_root) == 1


    #TODO: assert with str or other helper method when done
    def test_bst_depth_two(self, bst_depth_two):
        pass


    #TODO: assert with str or other helper method when done
    def test_bst_depth_three(self, bst_depth_three):
        pass


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
    #TODO: this needs to include tests at many recursive levels - see contains tests
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


class TestContainsPrivate:
    #TODO: implement this
    def test_something(self):
        pass


    def test_something_else(self):
        pass


class TestContains:
    ''' Tests on a BST with at least three levels are important because this
        implementation accesses/edits Nodes recursively through all levels.
    '''
    def test_found_from_root(self, bst_depth_two):
        t = bst_depth_two
        assert t.contains(20) == True


    @pytest.mark.parametrize('target', [
        (10),
        (30),
    ])
    def test_value_found_from_one_recursive_steps(self, target, bst_depth_two):
        t = bst_depth_two
        assert t.contains(target) == True


    @pytest.mark.parametrize('target', [
        (5),        # left left node
        (15),       # left right node
        (25),       # right left node
        (35),       # right right node
    ])
    def test_value_found_from_many_recursive_steps(self, target, bst_depth_three):
        t = bst_depth_three
        assert t.contains(target) == True


    @pytest.mark.parametrize('target', [
        (0),        # left node
        (100),      # right node
    ])
    def test_value_not_found_from_one_recursive_steps(self, target, bst_depth_two):
        t = bst_depth_two
        assert t.contains(target) == False


    @pytest.mark.parametrize('target', [
        (0),        # left node
        (100),      # right node
    ])
    def test_value_not_found_from_many_recursive_steps(self, target, bst_depth_three):
        t = bst_depth_three
        assert t.contains(target) == False


    def test_empty_tree_returns_false(self):
        t = BinarySearchTree()
        assert t.contains(1) == False
