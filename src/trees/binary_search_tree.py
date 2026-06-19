from typing import Optional
from stacks_and_queues.queue import LinkedListQueue as Queue


class BSTNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None


    def __str__(self):
        return(str(self.value))

    
    def __repr__(self):
        lv = None if self.left == None else self.left.value
        rv = None if self.right == None else self.right.value

        return(f'BST Node(value:{str(self.value)}, left:{lv}, right:{rv})')


class BinarySearchTree:
    ''' For simplicity, this tree will initially only handle integers.
    '''
    def __init__(self) -> None:
        self.root: Optional[BSTNode] = None
        self.size: int = 0


    def __len__(self) -> int:
        return self.size


    def _min_node(self, node: Optional[BSTNode]) -> BSTNode:
        ''' Gets the bottom left Node in Tree beginning from any 
        arbitrary Node.
        '''
        while node.left:
            node = node.left
        return node


    def _insert(self, node: Optional[BSTNode], value: int) -> BSTNode:
        ''' Recursevely redraws the path from root to new Node to maintain pointers to all
            updated child Nodes.
        '''
        if node is None:
            return BSTNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        if value > node.value:
            node.right = self._insert(node.right, value)

        if value == node.value:
            raise ValueError(f'{value} is already in this BST')

        return node


    def insert(self, value: int) -> None:
        try:
            self.root = self._insert(self.root, value)
        except ValueError as e:
            raise ValueError(f'duplicate error: {e}')
        else:
            self.size += 1


    def _delete(self, node: Optional[BSTNode], value: int) -> Optional[BSTNode]:
        ''' When the target Node is found the self._min_node() helper will
        search for the next highest value. It will always be in the bottom
        left of the subtree where the target Node's right branch is root.

        An opposite strategy may also be used where the next lowest value
        replaces the target which would always be found in the bottom right
        Node of the subtree beginning at the target Node's left branch.

        More simply put, in this implementation, the next highest leaf
        Node replaces the deleted target Node and is then deleted from
        it's original position.
        '''
        if node is None: 
            raise ValueError(f'{value} not found')

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            replacement = self._min_node(node.right)
            node.value = replacement.value
            node.right = self._delete(node.right, replacement.value)

        return node


    def delete(self, value: int) -> None: 
        ''' Raises ValueError if value is not found in BST. Logically, a
        ValueError will always raise if the BST is empty.
        '''
        try:
            self.root = self._delete(self.root, value)
        except ValueError as e:
            raise ValueError(f'delete error: {e}')
        else:
            self.size -= 1


    def _contains(self, node: Optional[BSTNode], value: int) -> bool:
        if node is None:
            return False
        elif value < node.value:
            return self._contains(node.left, value)
        elif value > node.value:
            return self._contains(node.right, value)
        else:
            # value == node.value
            return True


    def contains(self, value: int) -> bool:
        return self._contains(self.root, value)


    def _inorder(self, node: Optional[BSTNode], result: list[int]) -> None:
        if not node:
            return

        self._inorder(node.left, result)
        result.append(node.value)
        self._inorder(node.right, result)


    def inorder(self) -> list[int]:
        ''' In ascending order.
        '''
        result: list[int] = []
        self._inorder(self.root, result)
        return result


    def _preorder(self, node: Optional[BSTNode], result: list[int]) -> None:
        if not node:
            return

        result.append(node.value)
        self._preorder(node.left, result)
        self._preorder(node.right, result)


    def preorder(self) -> list[int]:
        ''' Top to bottom, left to right depth-first.
        '''
        result: list[int] = []
        self._preorder(self.root, result)
        return result


    def _postorder(self, node: Optional[BSTNode], result: list[int]) -> None:
        if not node:
            return

        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.value)


    def postorder(self) -> list[int]:
        ''' Bottom to top, left to right depth-first.
        '''
        result: list[int] = []
        self._postorder(self.root, result)
        return result


    def _levelorder(self, node: Optional[BSTNode], result: list[int], 
                    queue: Queue
                    ) -> None:
        if not node:
            return
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

        result.append(node.value)
        if not queue.is_empty():
            self._levelorder(queue.dequeue(), result, queue)


    def levelorder(self) -> list[int]:
        ''' Top to bottom, left to right breadth-first.
        '''
        result: list[int] = []
        queue: Queue[BSTNode] = Queue()
        self._levelorder(self.root, result, queue)
        return result


if __name__ == "__main__":
    n = BSTNode(42)
    print(type(n.value))
    print(type(n))
    print(repr(n))
