# Trees

| File | Structure | Note |
|:--|:--|:--|
| `binary_search_tree.py` | `BinarySearchTree` | provides average $O(\log n)$ time complexity for basic data operations |

---

## Description

Trees are non-linear data structures of nodes organized in hierarchical levels and branches. All branches originate from a common parent, top-level root node. Each node contains a value and zero or more pointers to child nodes.

Generally, trees are constructed, modified, and deconstructed using recursive techniques. Iterative approaches may be used to reduce space complexity and the number of function calls.

Applying certain invariants to Nodes create distinct types of Trees with benefitial attributes and behavior. See below for a detailed description and each included Tree.

---

## API

### Binary Search Tree

| Method | Time | Space | Notes |
|:--|:-:|:-:|:--|
| `insert()` / `_insert()`| $O(\log n)$<sup>(a)</sup> | $O(\log n)$<sup>(a)</sup> | Recursive implementation |
| `delete()` / `_delete()`| $O(\log n)$<sup>(a)</sup> | $O(\log n)$<sup>(a)</sup> | Recursive implementation |
| `contains()` / `_contains()`| $O(\log n)$<sup>(a)</sup> | $O(\log n)$<sup>(a)</sup> | Recursive implementation |
| `inorder()` / `_inorder()`| $O(n)$ | $O(n)$ | Depth-first Search (DFS) |
| `preorder()` / `_preorder()`| $O(n)$ | $O(n)$ | Depth-first Search (DFS)|
| `postorder()` / `_postorder()`| $O(n)$ | $O(n)$ | Depth-first Search (DFS) |
| `levelorder()` / `_levelorder()`| $O(n)$ | $O(w)$<sup>(b)</sup> | Breadth-first Search (BFS) |
| `height()` / `_height()`| $O(n)$ | $O(h)$<sup>(c)</sup> | Max depth calculation |

<sup>a</sup> Assuming the average case of a well-balanced tree, these methods execute in $O(h)$ where $h$ is the height of the tree ($h \approx \log n$). Highly skewed insertions (e.g., pre-sorted data) degrade performance to $O(n)$.
<sup>b</sup> Where $w$ is the width of the Tree ($w \approx \n/2$).
<sup>c</sup> Where $h$ is the height of the Tree ($h \approx \n/2$).

Any Node (N<sub>1</sub>) is allowed a maximum of two child Nodes (N<sub>2</sub>, N<sub>3</sub>). The value of N<sub>2</sub>, and all subsequent child nodes, must be lesser than the value of N<sub>1</sub>. It follows that the value of N<sub>3</sub>, and all subsequent child nodes, must be greater than the value of N<sub>1</sub>.

---

## Implementation Notes

**Binary Search Tree**<br>
The majority of the BST API is implemented using recursive helper patterns (`_method()`). The notable exception is `levelorder()`, which is implemented iteratively using a queue (in this case from `LinkedListQueue.py`). Breadth-First Search tracks nodes level-by-level, an iterative queue is more appropriate than a recursive call stack which acts more like a Stack.

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
- [ ] Implement iterative versions of contains() and insert() to achieve $O(1)$ space complexity.

