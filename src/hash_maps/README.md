# Hashmaps & Hashsets


| File | Structure | Notes |
|:--|:--|:--|
| `hashset.py` | `HashSet` | value store with linear probing to handle collisions |
| `hashmap.py` | `HashMap` | key/value store with list backed buckets for collisions|

---

## Description
Both structures use a hashing mechanism to perform basic data storage and access operations in constant ($O(1)$) time for the average case.
Both structures offer a similar API although under differently named methods. Internally, each is implemented to handle collisions differently.
To the external caller the important distinction is that a Hashmap will store satellite data with a provided key, whereas in a Hashset the value stored is used to generate the key.

---

## API

### HashSet

| Method | Time | Space | Notes |
|:--|:-:|:-:|:--|
| `set(value)` | $O(1)$<sup>(a)</sup> | $O(1)$<sup>(a)</sup> | Calls `_insert()` |
| `get(target)` | $O(1)$ | $O(1)$ | Calls `_scan_for_target()` |
| `delete(target)` | $O(1)$ | $O(1)$ | Calls `_scan_for_target()` |
| `_hash(value)` | $O(l)$<sup>(b)</sup> | $O(l)$<sup>(b)</sup> | Simple implementation for educational repo |
| `_probe(start)` | $O(1)$<sup>(c)</sup> | $O(1)$ | Generator function |
| `_get_next_index(index)` | $O(1)$ | $O(1)$ | Separated for testing |
| `_find_empty_bucket(index)` | $O(1)$<sup>(c)</sup> | $O(1)$ | Called `_probe()` only in event of a collision |
| `_scan_for_target(target)` | $O(1)$<sup>(c)</sup> | $O(1)$ | Calls `_probe()` |
| `_insert(value)` | $O(1)$ | $O(1)$ | This orchestrates calls to helpers with various average and worst cases |
| `_is_resize_required(count, capacity)` | $O(1)$ | $O(1)$ | Compares to a class constant |
| `_resize()` | $O(n)$ | $O(n)$ | Doubles storage capacity |
| `__str__()` | $O(n)$ | $O(1)$ | Returns list of Nodes by index |
| `__repr__()` | $O(1)$ | $O(1)$ | Returns attributes describing capacity of structure |
| `__len__()` | $O(1)$ | $O(1)$ | Returns `self.length` |

<sup>a</sup> When capacity threshold is reached the structure will automatically resize by rehashing every Node key. Resizing requires $O(n)$ time/space but is amortized over every non-resizing call to `set()`. 
<br>
<sup>b</sup> Hashing each character of a string is $O(k)$ where $k$ is the length of the string. For simplicity, I'll consider a call to hash to take constant time.
<br>
<sup>c</sup> The worst case is $O(n)$ but for simplicity I'm calling this $O(1)$

### HashMap

| Method | Time | Space | Notes |
|:--|:-:|:-:|:--|
| `put(key, value)` | $O(1)$<sup>(a)</sup> | $O(1)$<sup>(a)</sup> | Traverses list-backed bucket in event of collisions |
| `get(key, default)` | $O(1)$ | $O(1)$ | Searches list-backed bucket if necessary |
| `remove(key)` | $O(1)$ | $O(1)$ | Searches list-backed bucket if necessary |
| `contains(key)` | $O(k)$ | $O(1)$ | Traverses list where $k$ is link of the list |
| `_hash(value)` | $O(l)$<sup>(b)</sup> | $O(l)$<sup>(b)</sup> | Simple implementation for educational repo |
| `_resize()` | $O(n)$ | $O(n)$ | Doubles storage |
| `__len__()` | $O(1)$ | $O(1)$ | Returns `self.length` |

<sup>a</sup> When capacity threshold is reached the structure will automatically resize by rehashing every key. Resizing requires $O(n)$ time/space but is amortized over every non-resizing call to `put()`. 
<br>
<sup>b</sup> Hashing each character of a string is $O(l)$ where $l$ is the length of the string.

---

## Implementation Notes

**Hash Method**<br>
The hash method is intentionally simple for easily predictable collisions and simplistic tests as this is a learning/reference repo. I do not expect this to evenly distribute well across the list of buckets.

### HashSet

**Probe Traversal**<br> 
The generator method, probe, walks each `HashSet` bucket returning it's index number to the caller. Probe is capable of starting at any index and implicitly allows for one wrap to the beginning of the buckets. 

**Tombstone Pattern**<br>
The Singleton "tombstone" class is used by `HashSet` to treat buckets which were formerly occupied distinctly from those which are never used. This distinction matters when capacity is being recaptured by `_find_next_empty` and when searching for values impacted by collisions with `_scan_for_target`. 

### HashMap

**Bucket Datatype**<br>
Each entry is stored as a tuple of key/value pairs where key is a string and value is a variable, Generic datatype. Two alias types are provided in the global namespace to help with readability. 

**Get Method Default Argument**<br>
An optional argument is allowed in the get method to determine what the method call should return if the requested key is not found. The `Any` type is used here so that MyPy will let the caller pass any value here. This is probably nonsense but I wanted a reason to use the `Any` type hint. 

---

## Invariants

- Every non-empty bucket is either occupied or a tombstone (Hashset only).
- Total occupied buckets as a ratio of capacity is less than the maximum allowed load factor.
- Hashsets contain only unique values.
- Hashmaps contain unique keys but may contain duplicate values.

---

## TODOs and Questions

- test uniqueness invariants
- test falsy values in Hashmap.contains() because Hashmap.get() is returning value, not key, to the ternary.
- create a downsize method (opposed of resize)
