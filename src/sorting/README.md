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



---

## Algorithm Attributes

### Quadratic Sorts

| Method | Asymptotic Time | Avg Swap | Avg Compare | Aux Space |
|:--|:-:|:-:|:-:|:-: |
| `Insertion Sort()`| $O(n^2)$ | $\approx n(n-1)/4$ | $\approx (n(n-1)/4)+n$ | $O(1)$ |
| `Bubble Sort()` | $O(n^2)$ | $\approx n(n-1)/4$ | $n(n-1)/2$ | $O(1)$ |

**Insertion Sort**<br>
Starts from the beginning of an array and backtracks to previously sorted elements. Swaps any inverted values until a greater or equal value, or the beginning of the array, is encountered. Extremely efficient for nearly-sorted data.

**Bubble Sort**<br>
Compares adjacent elements and swaps them if they are in the wrong order. An outer loop narrows the unsorted search space, while the inner loop "bubbles" the target value to its correct boundary. Generally inefficient in practice compared to Insertion Sort due to excessive swap operations.

**Placeholder**<br>

---

## Implementation Notes

**Sorts Class**<br>
These sorting algorithms are wrapped in a unified Python tracking class. While sorting utilities are typically standalone functions, encapsulation allows internal instance counters to track exactly how many **swaps** and **comparisons** occur during execution. The test modules benchmark validation against theoretical bounds when running test suites.

**Bubble Sort**<br>
A traditional version moves the largest value to the right of the array. This implementation is the opposite and sometimes called a "shaker" or "bubble-down".

---

## Invariants

---

## TODOs and Questions
- [ ] Add `Selection Sort` to the quadratic module.
- [ ] Create divide and conquer method with `Merge Sort` and `Quick Sort`.

