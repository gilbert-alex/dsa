# Linked Lists

| File | Structure |
|---|---|
| `singly_linked_list.py` | `SinglyLinkedList` - head + tail pointers, forward traversal only |
| `doubly_linked_list.py` | `DoublyLinkedList` - head + tail pointers, bi-directional traversal |

---

## Description

A linked list is a linear data structure where elements (**nodes**) are connected
via pointers rather than stored contiguously in memory. Each node holds a value
and a reference to the next node. In a doubly linked list each node also holds a 
reference to the previous node.

To contrast a Python List which supports random indexing (i.e. my_list[0]), the
only way to reach a Linked List's Node is to traverse pointers from the head or
tail until the target node is found.

This lack of random indexing makes this structure relatively slow regarding search
methods but provides efficient insertion/deletion from the 'ends' of the list where
Lists/Arrays may have to reindex each element. It stands to reason that this
structure does not need much memory overhead to simply store pointers compared to
Lists/Arrays (but I dont know for sure and will find out more in this DSA project).

---

## API

### SinglyLinkedList

| Method | Time | Space | Notes |
|---|---|---|---|
| `prepend(value)` | O(1) | O(1) | Insert at head using head pointer |
| `append_slow(value)` | O(n) | O(1) | Insert at tail by traversal - tail pointer maintained but not used |
| `append_fast(value)` | O(1) | O(1) | Insert at tail using tail pointer |
| `delete(value)` | O(n) | O(1) | Deletes first occurrence; raises `ValueError` if not found |
| `count(target)` | O(n) | O(1) | Returns number of occurrences of target |
| `positions_of(target)` | O(n) | O(n) | Returns list of indicies where target is found |
| `to_list()` | O(n) | O(n) | Returns node values as a Python list |
| `__len__()` | O(1) | O(1) | Returns `self.length` |
| `__repr__()` | O(n) | O(n) | Debug string showing internal state and traversal |
| `__str__()` | O(n) | O(n) | Human-readable traversal string |

### DoublyLinkedList

| Method | Time | Space | Notes |
|---|---|---|---|
| `prepend(value)` | O(1) | O(1) | Insert at head; sets `next` and `previous` pointers |
| `append(value)` | O(1) | O(1) | Insert at tail; sets `next` and `previous` pointers |
| `delete_first(value, from_end=False)` | O(n) | O(1) | Deletes first occurrence from head or tail; raises `ValueError` if not found |
| `delete_all(value)` | O(n) | O(1) | Deletes all occurrences; raises `ValueError` if none found |
| `count(target)` | O(n) | O(1) | Returns number of occurrences of target |
| `positions_of(target)` | O(n) | O(n) | Returns list of indices where target is found |
| `to_list()` | O(n) | O(n) | Returns node values as a Python list |
| `__len__()` | O(1) | O(1) | Returns `self.length` |
| `__repr__()` | O(n) | O(n) | Debug strings showing internal state and traversal |
| `__str__()` | O(n) | O(n) | Human-readable traversal string |

---

## Implementation Notes

**Head and tail pointers are maintained on both structures.**<br>
This makes both `prepend` and `append` possible in O(1) time. The `append_slow` 
method on `SinglyLinkedList` is maintained to illustrate the benefit of a 
tail pointer.

**`delete` on `SinglyLinkedList` deletes the first occurrence.**<br> 
Traversal of a singly linked list is always required to discover the previous 
node in order to link around the target node.

**`delete_first` on `DoublyLinkedList` accepts a `from_end` flag.**<br>
Because the DLL has a `previous` pointer, you can traverse from either end. 
Creating a separate `delete_last` method would be cleaner but this is an 
intentional experiment with a different technique.

**Both delete methods raise `ValueError` when the target is not found.**

**`_make_sll` and `_make_dll` are test helper functions.**<br>
They allow tests to bypass the public interface while building lists to decouple 
setup from the methods under test. In other words, you shouldn't use a separate 
public method to setup a teGst for a different public method. 

---

## Invariants

Every mutating operation must leave the structure in a consistent state. These
invariants hold after every method call:

- If `length == 0`: `head is None` and `tail is None`
- If `length == 1`: `head is tail` and `head.next is None`
- `tail.next` is always `None`
- `head.previous` is always `None` (DLL only)
- For every node `n` with a successor `s`: `n.next is s` and `s.previous is n` (DLL only)

---

## TODOs and Questions

- Implement invariant test helper function and include in unit tests.
- Refactor the removal of a node to a `_unlink_node` private method.
- Rename directory to drop reference to array.
- Can I refactor these classes to better use self.head|tail to more 
  elegantly traverse.
