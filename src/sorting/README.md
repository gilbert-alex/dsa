# Sorting Algorithms

| File | Strategy / Category | Primary Operational Profile |
|:--|:-:|:--|
| `quadratic_sorts.py` | Comparison / Iterative | Small arrays, stable, $O(1)$ auxiliary memory. |
| `divide_conquer_sorts.py` | Comparison / Recursive | Large datasets, predictable scaling ($O(n \log n)$). |
| `linear_time_sorts.py` | Non-Comparison / Distribution | Integer/String keys with bounded ranges ($O(n)$). |
| `heap_sorts.py` | Comparison / Selection | Priority queue based, guaranteed $O(n \log n)$ in-place. |
| `tree_sorts.py` | Comparison / Insertion | Uses a Binary Search Tree structure. |
---

## Description
The invariants listed for each algorithm below must be true at each of three different points: 1) before any loop iteration, 2) after each loop iteration, and 3) after all loop iterations.

Typically, sorting algorithms are used to modify the order of records. Records are made up of two parts; a key, and satellite data. These algorithms operate on the keys which, in this repo, i've chosen to simplify to a simple list of integers. 

After an algorithm has been tested to it's theoretical benchmarks I'll modify the API to sort not only a list of integers but a list of records by an arbitary key field. For example, the Insertion Sort API is modified to include an anomious function to accessing a named dictionary field. If written literally, the keys would resolve to `array[index][named_field]` if accessing a string literal list of dictionaries. 

---

## Algorithms 

### Quadratic Sorts

| Method | Asymptotic Time | Avg Swap | Avg Compare | Aux Space |
|:--|:-:|:-:|:-:|:-: |
| `Insertion Sort()`| $O(n^2)$ | $\approx n(n-1)/4$ | $\approx (n(n-1)/4)+n$ | $O(1)$ |
| `Bubble Sort()` | $O(n^2)$ | $\approx n(n-1)/4$ | $n(n-1)/2$ | $O(1)$ |

#### Insertion Sort
**Description**<br>
Starts from the beginning of an array and backtracks over previously sorted keys swapping any inversions until a greater or equal value, or the beginning of the array, is encountered. Efficient for nearly-sorted data.

**Invariants**<br>
The subarray `A[0:i-1]` consists of the same elements origionally in the same subarray but in sorted order.

#### Bubble Sort
**Description**<br>
Compares adjacent keys and swaps them if they are in the wrong order. An outer loop narrows the unsorted search space, while the inner loop "bubbles" the target value to its correct boundary. Generally inefficient due to excessive swap operations.

**Invariants**<br>
placeholder

**Placeholder**<br>

---

## Implementation Notes

**Sorts Class**<br>
These sorting algorithms are wrapped in a unified Python tracking class. While sorting utilities are typically standalone functions, encapsulation allows internal instance counters to track exactly how many **swaps** and **comparisons** occur during execution. The test modules benchmark validation against theoretical average case boundaries.

**Bubble Sort**<br>
A traditional version moves the largest value to the right of the array. This implementation is the opposite and sometimes called a "shaker" or "bubble-down".

---

## TODOs and Questions
- [ ] Add `Selection Sort` to the quadratic module.
- [ ] Create divide and conquer method with `Merge Sort` and `Quick Sort`.

