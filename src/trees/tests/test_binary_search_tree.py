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


def assert_bst_invariant(node, low=None, high=None):
    ''' Recursive helper to check that left pointers are to nodes with
        smaller values and right pointers are to nodes with higher values.
    '''
    if node is None:
        return
    assert low is None or node.value > low
    assert high is None or node.value < high
    return assert_bst_invariant(node.left, low, node.value)
    return assert_bst_invariant(node.right, node.value, high)


class TestSetup:
    @pytest.mark.parametrize('tree_fixture', [
        "bst_only_root",
        "bst_depth_two",
        "bst_depth_three",
    ])
    def test_invariants(self, tree_fixture, request):
        t = request.getfixturevalue(tree_fixture)
        assert_bst_invariant(t.root)


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
    def test_empty_tree_returns_new_node(self):
        t = BinarySearchTree()
        result = t._insert(t.root, 1)
        assert type(result).__name__ == "BSTNode"


    def test_smaller_value_update_left_pointer(self, bst_only_root):
        t = bst_only_root
        t._insert(t.root, 9)
        assert t.root.left != None
        assert t.root.right == None


    def test_smaller_value_update_right_pointer(self, bst_only_root):
        t = bst_only_root
        t._insert(t.root, 11)
        assert t.root.left == None
        assert t.root.right != None


    def test_new_node_has_null_pointers(self, bst_only_root):
        t = bst_only_root
        t._insert(t.root, 1)
        new_node = t.root.left
        assert new_node.left == None
        assert new_node.right == None


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


    def test_root_address_changes_when_set(self):
        t = BinarySearchTree()
        initial_address = id(t.root)
        t.insert(50)
        assert initial_address != id(t.root)


    def test_static_root_addr_for_new_child(self, bst_only_root):
        t = bst_only_root
        initial_address = id(t.root)
        t.insert(1)
        assert initial_address == id(t.root)


    def test_static_root_addr_for_new_distant_child(self, bst_depth_three):
        t = bst_depth_three
        initial_address = id(t.root)
        t.insert(1)
        assert initial_address == id(t.root)


    def test_static_inter_addr_for_new_child(self, bst_depth_two):
        t = bst_depth_two
        initial_address = id(t.root.left)
        t.insert(1)
        assert initial_address == id(t.root.left)


    def test_static_inter_addr_for_new_distant_child(self, bst_depth_three):
        t = bst_depth_three
        initial_address = id(t.root.left)
        t.insert(1)
        assert initial_address == id(t.root.left)


    def test_insert_duplicate_raises(self):
        t = BinarySearchTree()
        t.insert(2)
        with pytest.raises(ValueError) as e:
            t.insert(2)
        assert str(e.value) == '2 is already in this BST'


    @pytest.mark.parametrize('nodes', [
        ([20, 10, 30, 5, 15, 25, 35, 4, 6, 14, 16, 24, 26, 34, 36]),    #balanced
        ([20, 19, 18, 17, 16, 15]),                 #ordered desc
        ([1, 2, 3, 4, 5, 6, 7, 8, 9]),              #ordered asc
        ([10, 1, 9, 2, 8, 3, 7, 4, 6, 5]),          #all less than root
        ([1, 10, 2, 9, 3, 8, 4, 7, 5, 6]),          #all greater than root
        ([-5, -6, -7]),                             #negative integers
        ([0, -2, 2, -3, -1, 1, 3]),                 #include zero
        ([1, 5, 4, 6, 2]),                          #insert at intermediate depth
    ])
    def test_unittest(self, nodes):
        t = BinarySearchTree()
        for n in nodes:
            t.insert(n)
        assert_bst_invariant(t.root)
        assert len(t) == len(nodes)
    

class TestContainsPrivate:
    def test_false_for_empty_tree(self):
        t = BinarySearchTree()
        assert t._contains(t.root, 1) == False


    def test_finds_left_child(self, bst_depth_two):
        t = bst_depth_two
        assert t._contains(t.root, 10)


    def test_finds_right_child(self, bst_depth_two):
        t = bst_depth_two
        assert t._contains(t.root, 30)


    def test_finds_left_child_with_recursion(self, bst_depth_three):
        t = bst_depth_three
        assert t._contains(t.root, 5)


    def test_finds_right_child_with_recursion(self, bst_depth_three):
        t = bst_depth_three
        assert t._contains(t.root, 35)


    @pytest.mark.parametrize('target', [
        -1, 0, 4, 6, 9, 11, 14, 16, 19, 21, 24, 26, 29, 31, 24, 36,
    ])
    def test_false_with_recursion(self, target, bst_depth_three):
        t = bst_depth_three
        assert t._contains(t.root, target) == False


class TestContains:
    ''' Tests on a BST with at least three levels are important because this
        implementation accesses/edits Nodes recursively through all levels.
    '''
    def test_finds_root(self, bst_depth_two):
        t = bst_depth_two
        r = t.root.value
        assert t.contains(r) == True


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
