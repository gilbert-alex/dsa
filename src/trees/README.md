# Trees

| File | Structure | Note |
|:--|:--|:--|
| `binary_search_tree.py` | `BinarySearchTree` | |

---

## Description

Trees are non-linear data structures of nodes organized in hierarchial levels and branches. All branches originate from a common parent, top-level root node. Each node contains a value and zero or more pointers to child nodes.

Generally, trees are constructed, modified, and deconstructed using recursive techniques. 

Applying certain invariants to Nodes create distinct types of Trees with benefitialattributes and behavior. See below for a detailed description and each included Tree.

---

## API

### Binary Search Tree

| Method | Time | Space | Notes |
|---|---|---|---|
| `insert()`<br>`_insert()`| $O(\log n)$<sup>(a)</sup> | $O(\log n)$<sup>(a)</sup> | Assuming a recursive implementation |
| `delete()`<br>`_delete()`| $O(\log n)$<sup>(a)</sup> | $O(\log n)$<sup>(a)</sup> | Assuming a recursive implementation |
| `contains()`<br>`_contains()`| $O(\log n)$<sup>(a)</sup> | $O(\log n)$<sup>(a)</sup> | Assuming a recursive implementation |
| `inorder()`<br>`_inorder()`| O(n) | O(n) | |
| `preorder()`<br>`_preorder()`| O(n) | O(n) | |
| `postorder()`<br>`_postorder()`| O(n) | O(n) | |
| `levelorder()`<br>`_levelorder()`| O(n) | O(n) | |
| `height()`<br>`_height()`| O(n) | O(n) | |

<sup>a</sup> Assuming the average case of a well-distributed Tree, these methods will execute in O(h) where h is the height of the Tree.

Any Node (N<sub>1</sub>) is allowed a maximum of two child Nodes (N<sub>2</sub>; N<sub>3</sub>). The value of N<sub>2</sub>, and all subsequent child nodes, must be lesser than the value of N<sub>1</sub>. It follows that the value of N<sub>3</sub>, and all subsequent child nodes, must be greater than the value of N<sub>1</sub>.

---

## Implementation Notes

**Binary Search Tree**<br>
This tree is implemented largely with recursive calls. Different space complexity may be accomplished with an itterative approach. The notable exception is that `levelorder()` is implemented iteratively as most language compilers have a maximum size for the call stack. In Python, the default setting is 1,000 and raises a `RecursionError`.

**title**<br>

**title**<br>


---

## Invariants

Generally, the following attributes are true for all Trees.

  - Any Node can be reached from the Root.
  - Only one path exists between any Node and the Root.
  - Every Node, except the Root, must have one, and only one, parent Node.
  - For a Tree of size n, there will be n-1 Edges.
  - Circular paths or loops between Nodes cannot exist.

---

## TODOs and Questions
- 

