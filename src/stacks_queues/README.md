# Stacks & Queues

| File | Structure | Note |
|:--|:--|:--|
| `queue.py` | `ListQueue` | Implemented with a Python List |
| `queue.py` | `LinkedListQueue` | Implemented with a Linked List |
| `stack.py` | `ListStack` | Implemented with a Python List |
| `stack.py` | `LinkedListStack` | Implemented with a Linked List |

---

## Description

Stacks and Queues are linear collections of items stored and/or accessed 
in an routine, but different, order. Stacks are accessed 
'Last In First Out' (LIFO) and Queues are accessed 'First in First Out' (FIFO). 

Time complexity considerations are most important at insertion and deletion
operations. An efficient structure is capable of performing both operations
at constant time. 

In this project, both structures are implemented twice in each module. One with
a Python List backed structure and another with a Singly Linked List (inself
implemented at `dsa/src/linked_lists/singly_linked_list.py`) to explore the 
effect on insertion/deletion time complexity.

---

## API

### Stack

| Method | Time | Space | Time | Space |
|:--|:-:|:-:|:-:|:-:|
| | **List** | | **Linked List** | |
| `push(item)` | O(1) | O(1) | O(1) | O(1) |
| `pop()` | O(1) | O(1) | O(1)<sup>(a)</sup> | O(1) |
| `peek()` | O(1) | O(1) | O(1) | O(1) |
| `is_empty()` | O(1) | O(1) | O(1) | O(1) |

### Queue

| Method | Time | Space | Time | Space |
|:--|:-:|:-:|:-:|:-:|
| | **List** | | **Linked List** | |
| `enqueue(item)` | O(1) | O(1) | O(1) | O(1) |
| `dequeue()` | O(n)<sup>(b)</sup> | O(1) | O(1)<sup>(b)</sup> | O(1) |
| `peek()` | O(1) | O(1) | O(1) | O(1) |
| `is_empty()` | O(1) | O(1) | O(1) | O(1) |

<sup>a</sup> Although sll.delete() has O(n) worst case, this implementation operates in O(1). (see Issue #4)
<br>
<sup>b</sup> Time complexity improved to O(1) by use of a linked list backed structure removing the need to reindex an entire list upon Node removal.

---

## Implementation Notes

**Each module contains two classes**<br>
List and Linked List backed classes are included in each module. Both structures
have the same API.

**String representation and mental model**<br>
When printed to the terminal, I visualized Stacks/Queues as [Front <- ... <- Back].
Probably because it was natural to do so when reading left to right. However,
Python built-in List methods operate on the n-th side of a List. The str
and repr dunder methods display items in the order I visualize the structures.

**Stack implementations**<br>
Python Lists append/pop from the n-th index which nicely avoids indexing all
items on insertion/deletion. The only oddity in the List-backed Stack is that
the string representations must be reversed to fit my mental model discussed
above.

**Trade-offs in List-backed Queue**<br>
New items are appended to the right of the list at O(1). Removal from the left 
requires O(n) as each remaining element must be reindexed. Alternatively, 
inserting at index 0 would invert these costs.

**Queue optimization with Linked-list backed structure**<br>
Reimplementing the Queue with a linked list improves deletion complexity to
O(1) because we can access the head directly and efficiently update pointers
to the next item. Reindexing all items is not necessary as in the List-backed
Queue.

---

## Invariants

These are simply wrappers around their underlying data structures. As such, 
there are no invariants to consider discretly from the underlying implementation.

---

## TODOs and Questions
- Implement LinkedListStack.delete_head() and LinkedListQueue.delete_head() as
  helper for LinkedListStack.pop() and LinkedListQueue.dequeue(), respectively. (Issue #4)
