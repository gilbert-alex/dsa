from typing import Any, Optional


class BSTNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[BST_Node] = None
        self.right: Optional[BST_Node] = None


    def __str__(self):
        return(str(self.value))

    
    def __repr__(self):
        lv = None if self.left == None else self.left.value
        rv = None if self.left == None else self.right.value

        return(f'BST Node(value:{str(self.value)}, left:{lv}, right:{rv})')


class BinarySearchTree:
    ''' For simplicity, this tree will initially only handle integers.
    '''
    def __init__(self) -> None:
        self.root: Optional[BSTNode] = None
        self.size: int = 0


    def __len__(self) -> int:
        return self.size


    def _insert(self, node: Optional[BSTNode], value: int) -> BSTNode | None:
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
            raise e
        else:
            self.size += 1


    def _remove(self, node: Optional[BSTNode], value: int):
        pass 


    def remove(self, value: int) -> int | None:
        pass


    def _contains(self, node: Optional[BSTNode], value: int) -> bool:
        if node is None:
            return False
        if value < node.value:
            return self._contains(node.left, value)
        if value > node.value:
            return self._contains(node.right, value)
        if value == node.value:
            return True


    def contains(self, value: int) -> bool:
        return self._contains(self.root, value)


if __name__ == "__main__":
    n = BSTNode(42)
    print(type(n.value))
    print(type(n))
    print(repr(n))
