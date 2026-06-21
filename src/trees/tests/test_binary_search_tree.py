import sys
import random
import pytest
from ..binary_search_tree import BSTNode, BinarySearchTree

REALLY_BIG_TREE_SIZE = 2000

@pytest.fixture
def bst_only_root():
    t = BinarySearchTree()
    t.root = BSTNode(10)
    t.size += 1
    return t


@pytest.fixture                         #      20
def bst_depth_two():                    #     /  \
    t = BinarySearchTree()              #   10    30
    t.root = BSTNode(20)
    t.root.left = BSTNode(10)
    t.root.right = BSTNode(30)
    t.size += 3
    return t


@pytest.fixture                         #      20
def bst_depth_three(bst_depth_two):     #     /  \
    t = bst_depth_two                   #   10    30
    left_child = t.root.left            #  /  \   / \
    left_child.left = BSTNode(5)        # 5   15 25  35
    left_child.right = BSTNode(15)
    right_child = t.root.right
    right_child.left = BSTNode(25)
    right_child.right = BSTNode(35)
    t.size += 4
    return t


@pytest.fixture
def bst_really_big():
    ''' This try/catch block is intented to identify RecursionErrors happening
    in the build of the tree. With a 100k range for random ints, this build 
    raised RecursionError at the following:
        run 1: i = 2,906; h = 961
        run 2: i = 9,920; h = 961
        run 3: i = 2,915; h = 961
        run 4: i = 2,808; h = 961 
        run 5: i = 2,884; h = 961 

    The note above applies to this code which provides an insufficiently 
    distributed sample for proper use of a tree structure. Replaced with the
    random.sample() expression below. The build succeeds with random.sample()
    even if the range == the size of the sample.

    unique_values = set()
    while len(unique_values) < 5000:
        unique_values.add(random.randint(1, 100000))
    '''
    t = BinarySearchTree()
    unique_values = random.sample(range(1, REALLY_BIG_TREE_SIZE*10), REALLY_BIG_TREE_SIZE)
    try:
        for i, v in enumerate(unique_values):
            t.insert(v)
    except RecursionError:
        print(f'insertion completed: {i}')
        print(f'tree height at failure: {t.height(t.root)}')
        raise
    # This msg will print to stdout on any test fail using this fixture
    # To see this value w/o failures run with `pytest -s`
    print(f'\nBST height is: {t.height(t.root)}')      
    return t


def assert_bst_invariant(node, low=None, high=None):
    '''Recursive helper to check that left pointers are to nodes with
        smaller values and right pointers are to nodes with higher values.
    '''
    if node is None:
        return
    assert low is None or node.value > low
    assert high is None or node.value < high
    assert_bst_invariant(node.left, low, node.value)
    assert_bst_invariant(node.right, node.value, high)

def collect_pointers(node):
    if node is None:
        return []
    return (
        [(id(node), node.value, id(node.left), id(node.right))]
        + collect_pointers(node.left)
        + collect_pointers(node.right)
    )


class TestSetup:
    @pytest.mark.parametrize('tree_fixture', [
        "bst_only_root",
        "bst_depth_two",
        "bst_depth_three",
    ])
    def test_fixture_invariants(self, tree_fixture, request):
        t = request.getfixturevalue(tree_fixture)
        assert_bst_invariant(t.root)


    def test_bst_depth_two(self, bst_depth_two):
        t = bst_depth_two
        assert t.inorder() == [10, 20, 30]


    def test_bst_depth_three(self, bst_depth_three):
        t = bst_depth_three
        assert t.inorder() == [5, 10, 15, 20, 25, 30, 35]


    def test_bst_really_big(self, bst_really_big):
        t = bst_really_big
        assert len(t) == REALLY_BIG_TREE_SIZE
        assert_bst_invariant(t.root)


class TestBSTNode:
    def test_init(self):
        n = BSTNode(5)
        assert n.value == 5
        assert n.left is None
        assert n.right is None


class TestBinarySearchTree:
    def test_init(self):
        t = BinarySearchTree()
        assert t.root is None
        assert len(t) == 0


    def test_component(self):
        #TODO: do this when core BST methods are in place
        pass


class TestMinimumNode:
    def test_start_search_from_root_node(self, bst_depth_three):
        t = bst_depth_three
        assert t._min_node(t.root).value == 5


    def test_start_search_from_intermediate_node(self, bst_depth_three):
        t = bst_depth_three
        n = t.root.left
        assert t._min_node(n).value == 5


    def test_start_search_from_leaf_node(self, bst_depth_three):
        t = bst_depth_three
        n = t.root.left.left
        assert t._min_node(n).value == 5


    def test_returns_node_without_left_child(self, bst_only_root):
        t = bst_only_root
        t.root.right = BSTNode(20)
        assert t._min_node(t.root).value == 10


    def test_returns_intermediate_node(self, bst_only_root):
        t = bst_only_root
        t.root.left = BSTNode(1)
        t.root.left.right = BSTNode(4)
        t.root.left.right.left = BSTNode(3)
        t.root.left.right.right = BSTNode(5)
        assert t._min_node(t.root).value == 1


class TestInsertPrivate:
    def test_empty_tree_returns_new_node(self):
        t = BinarySearchTree()
        result = t._insert(t.root, 1)
        assert type(result).__name__ == "BSTNode"


    def test_smaller_value_update_left_pointer(self, bst_only_root):
        t = bst_only_root
        t._insert(t.root, 9)
        assert t.root.left is not None
        assert t.root.right is None


    def test_smaller_value_update_right_pointer(self, bst_only_root):
        t = bst_only_root
        t._insert(t.root, 11)
        assert t.root.left is None
        assert t.root.right is not None


    def test_new_node_has_null_pointers(self, bst_only_root):
        t = bst_only_root
        t._insert(t.root, 1)
        new_node = t.root.left
        assert new_node.left is None
        assert new_node.right is None


    def test_insert_duplicate_raises(self, bst_only_root):
        t = bst_only_root
        with pytest.raises(ValueError) as e:
            t._insert(t.root, 10)
        assert str(e.value) == '10 is already in this BST'


class TestInsert:
    def test_set_root(self):
        t = BinarySearchTree()
        assert t.root is None
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
        assert initial_address is not id(t.root)


    def test_static_root_addr_for_new_child(self, bst_only_root):
        '''This works but it's a lotta lines for the next few tests
        '''
        t = bst_only_root
        target = 10
        before = collect_pointers(t.root)
        before_node = next((n[:2] for n in before if n[1] == target), None)
        t.insert(1)
        after = collect_pointers(t.root)
        after_node = next((n[:2] for n in after if n[1] == target), None)
        assert after_node == before_node


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
        assert str(e.value) == 'duplicate error: 2 is already in this BST'


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
    

class TestDeletePrivate:
    ''' The return value will be the root pointer to the entire structure.
    Therefore, I can save the method's return value to a variable and test
    that to the invariant helper.
    '''
    def test_empty_tree_raises(self):
        t = BinarySearchTree()
        with pytest.raises(ValueError) as e:
            t._delete(t.root, 1)
        assert str(e.value) == '1 not found'


    def test_not_found_in_deep_tree_raises(self, bst_depth_three):
        t = bst_depth_three
        with pytest.raises(ValueError) as e:
            t._delete(t.root, 100)
        assert str(e.value) == '100 not found'


    def test_failed_delete_leaves_tree_unmodified(self, bst_depth_three):
        t = bst_depth_three
        before = collect_pointers(t.root)
        with pytest.raises(ValueError):
            t._delete(t.root, 100)
        
        after = collect_pointers(t.root)
        assert before == after
        assert len(t) == 7


    #      20
    #     /  \
    #   10    30
    #  /  \   / \
    # 5   15 25  35
    def test_delete_mutates_target_pointer(self, bst_depth_three):
        t = bst_depth_three
        target = 30

        before = collect_pointers(t.root)
        #n[1] is the node's value
        before_node = next((n for n in before if n[1] == target), None)
        target_address = before_node[0]

        t._delete(t.root, target)

        after = collect_pointers(t.root)
        after_node = next((n for n in after if n[0] == target_address), None)

        assert before_node[0] == after_node[0]      #node address
        assert before_node[1] != after_node[1]      #node value
        assert before_node[2] == after_node[2]      #left pointer address
        assert before_node[3] != after_node[3]      #right pointer address
        assert after_node[1] != target
        

    def test_delete_left_leaf_mutates_parent_pointer(self, bst_depth_three):
        t = bst_depth_three
        before = collect_pointers(t.root)
        
        delete_value = 5
        delete_address = next((n[0] for n in before if n[1] == delete_value), None)

        #n[2] is the parent node's left pointer
        before_node = next((n for n in before if n[2] == delete_address), None)
        target_address = before_node[0]

        t._delete(t.root, delete_value)

        after = collect_pointers(t.root)
        after_node = next((n for n in after if n[0] == target_address), None)
        
        assert before_node[0] == after_node[0]      #node address
        assert before_node[1] == after_node[1]      #node value
        assert before_node[2] != after_node[2]      #left pointer address
        assert before_node[3] == after_node[3]      #right pointer address


    def test_delete_right_leaf_mutates_parent_pointer(self, bst_depth_three):
        t = bst_depth_three
        before = collect_pointers(t.root)
        
        delete_value = 15
        delete_address = next((n[0] for n in before if n[1] == delete_value), None)

        #n[2] is the parent node's left pointer
        before_node = next((n for n in before if n[3] == delete_address), None)
        target_address = before_node[0]

        t._delete(t.root, delete_value)

        after = collect_pointers(t.root)
        after_node = next((n for n in after if n[0] == target_address), None)
        
        assert before_node[0] == after_node[0]      #node address
        assert before_node[1] == after_node[1]      #node value
        assert before_node[2] == after_node[2]      #left pointer address
        assert before_node[3] != after_node[3]      #right pointer address


class TestDelete:
    def test_removes_root(self, bst_only_root):
        t = bst_only_root
        assert t.root is not None
        t.delete(10)
        assert t.root is None


    def test_size_decrements_to_zero(self, bst_only_root):
        t = bst_only_root
        initial_size = len(t)
        t.delete(t.root.value)
        assert len(t) == initial_size -1


    def test_delete_decrements_size(self, bst_depth_two):
        t = bst_depth_two
        initial_size = len(t)
        t.delete(30)
        assert len(t) == initial_size - 1


    def test_delete_intermediate_node(self, bst_depth_three):
        t = bst_depth_three
        t.delete(10)
        assert_bst_invariant(t.root)


    def test_not_found_raises(self, bst_depth_three):
        t = bst_depth_three
        with pytest.raises(ValueError) as e:
            t.delete(100)
        assert str(e.value) == 'delete error: 100 not found'


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


    def test_finds_left_child_at_depth(self, bst_depth_three):
        t = bst_depth_three
        assert t._contains(t.root, 5)


    def test_finds_right_child_at_depth(self, bst_depth_three):
        t = bst_depth_three
        assert t._contains(t.root, 35)


    @pytest.mark.parametrize('target', [
        -1, 0, 4, 6, 9, 11, 14, 16, 19, 21, 24, 26, 29, 31, 24, 36,
    ])
    def test_not_found_at_depth(self, target, bst_depth_three):
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


class TestInOrder:
    def test_empty_tree_returns_empty_list(self):
        t = BinarySearchTree()
        assert t.inorder() == []


    def test_left_branch_only(self):
        t = BinarySearchTree()
        for n in [10, 12, 11, 13]:
            t.insert(n)
        assert t.inorder() == [10, 11, 12, 13]


    def test_right_branch_only(self):
        t = BinarySearchTree()
        for n in [10, 8, 9, 7]:
            t.insert(n)
        assert t.inorder() == [7, 8, 9, 10]


    def test_full_tree(self, bst_depth_three):
        t = bst_depth_three
        assert t.inorder() == [5, 10, 15, 20, 25, 30, 35]


    def test_length_matches_tree_size(self, bst_really_big):
        t = bst_really_big
        result = t.inorder()
        assert len(result) == len(t)


class TestPreOrder:
    def test_empty_tree_returns_empty_list(self):
        t = BinarySearchTree()
        assert t.preorder() == []


    def test_left_branch_only(self):
        t = BinarySearchTree()
        for n in [10, 12, 11, 13]:
            t.insert(n)
        assert t.preorder() == [10, 12, 11, 13]


    def test_right_branch_only(self):
        t = BinarySearchTree()
        for n in [10, 8, 9, 7]:
            t.insert(n)
        assert t.preorder() == [10, 8, 7, 9]


    def test_full_tree(self, bst_depth_three):
        t = bst_depth_three
        assert t.preorder() == [20, 10, 5, 15, 30, 25, 35]


    def test_length_matches_tree_size(self, bst_really_big):
        t = bst_really_big
        result = t.preorder()
        assert len(result) == len(t)


class TestPostOrder:
    def test_empty_tree_returns_empty_list(self):
        t = BinarySearchTree()
        assert t.postorder() == []


    def test_left_branch_only(self):
        t = BinarySearchTree()
        for n in [10, 12, 11, 13]:
            t.insert(n)
        assert t.postorder() == [11, 13, 12, 10]


    def test_right_branch_only(self):
        t = BinarySearchTree()
        for n in [10, 8, 9, 7]:
            t.insert(n)
        assert t.postorder() == [7, 9, 8, 10]


    def test_full_tree(self, bst_depth_three):
        t = bst_depth_three
        assert t.postorder() == [5, 15, 10, 25, 35, 30, 20]


    def test_length_matches_tree_size(self, bst_really_big):
        t = bst_really_big
        result = t.postorder()
        assert len(result) == len(t)


class TestLevelOrder:
    def test_empty_tree_returns_empty_list(self):
        t = BinarySearchTree()
        assert t.levelorder() == []


    def test_left_branch_only(self):
        t = BinarySearchTree()
        for n in [10, 12, 11, 13]:
            t.insert(n)
        assert t.levelorder() == [10, 12, 11, 13]


    def test_right_branch_only(self):
        t = BinarySearchTree()
        for n in [10, 8, 9, 7]:
            t.insert(n)
        assert t.levelorder() == [10, 8, 7, 9]


    def test_full_tree(self, bst_depth_three):
        t = bst_depth_three
        assert t.levelorder() == [20, 10, 30, 5, 15, 25, 35]


    def test_length_matches_tree_size(self, bst_really_big):
        t = bst_really_big
        result = t.levelorder()
        assert len(result) == len(t)
