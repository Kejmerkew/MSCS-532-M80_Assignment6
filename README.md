# Part 1: Implementation and Analysis of Selection Algorithms

## Implemented Algorithms

### 1. **Deterministic Selection (Median of Medians)**
- Guarantees **O(n)** time complexity in the **worst case**.  
- Works by dividing the array into groups of five, finding medians recursively, and using the median of these medians as a pivot.  
- Provides stability and predictable performance even on adversarial inputs.

### 2. **Randomized Selection (Quickselect)**
- Achieves **O(n)** time on **average** but may degrade to **O(n²)** in the worst case.  
- Randomly chooses a pivot for partitioning, which works efficiently for most real-world datasets.

---

## How to Run

### **1. Clone or Download the Repository & Run program**
```bash
git clone https://github.com/Kejmerkew/MSCS-532-M80_Assignment6
cd Code
python SelectionAlgorithms.py
```

### **2. Output will look like this:**
```
=== Benchmark: Deterministic vs Randomized Selection ===

Input size: 1000
    random | Deterministic: 0.39 ms | Randomized: 0.39 ms
    sorted | Deterministic: 0.32 ms | Randomized: 0.10 ms
  reversed | Deterministic: 0.32 ms | Randomized: 0.13 ms
duplicates | Deterministic: 0.15 ms | Randomized: 0.07 ms

Input size: 5000
    random | Deterministic: 1.09 ms | Randomized: 1.52 ms
    sorted | Deterministic: 1.65 ms | Randomized: 1.05 ms
  reversed | Deterministic: 1.72 ms | Randomized: 1.21 ms
duplicates | Deterministic: 0.78 ms | Randomized: 0.68 ms

Input size: 10000
    random | Deterministic: 4.16 ms | Randomized: 1.55 ms
    sorted | Deterministic: 3.47 ms | Randomized: 1.78 ms
  reversed | Deterministic: 3.53 ms | Randomized: 3.09 ms
duplicates | Deterministic: 1.56 ms | Randomized: 1.74 ms

Benchmark completed.

```

## Summary of Findings
### Theoretical Analysis

* Deterministic (Median of Medians): Achieves true O(n) performance in the worst case by ensuring balanced partitions.
* Randomized (Quickselect): Expected time complexity of O(n), though rare worst-case inputs may reach O(n²).
* Space Complexity: Both algorithms are O(1) for in-place partitioning (aside from recursion overhead).

### Empirical Results

* For small inputs, both algorithms performed similarly.
* On sorted and reversed data, the randomized approach was faster due to simpler partitioning.
* For larger arrays, the deterministic algorithm showed stable and predictable performance, confirming its resilience to input ordering.
* The overall empirical trend matches theoretical expectations: Randomized Quickselect tends to outperform on average, but Median of Medians guarantees consistency.

---
# Part 2: Elementary Data Structures Implementation and Discussion
---

## Implementation Details

### Implemented Data Structures
- **Array:** Supports insertion, deletion, and element access.  
- **Stack:** Implemented using an array with push and pop operations.  
- **Queue:** Implemented using an array with enqueue and dequeue operations.  
- **Linked List:** Implements node-based insertion, deletion, and traversal.

Each data structure is implemented **from scratch** to provide a deeper understanding of their underlying mechanics and efficiency trade-offs.

---

## How to Run

### **1. Clone or Download the Repository**
```bash
git clone https://github.com/Kejmerkew/MSCS-532-M80_Assignment6
cd Code
python DataStructures.py
```

### **2. Output will look like this:**
```
=== Demonstrating Elementary Data Structures ===
Array: [10, 30]
Stack: [5]
Queue: [2]
Linked List: 10 -> 30
```

## Summary of Findings
Arrays are faster for random access, while linked lists are better for frequent insertions or deletions. When stacks and queues are implemented using arrays, they offer faster fixed-size performance but can suffer from costly resizing. Linked lists, however, provide more flexible memory management with minimal overhead for dynamic growth.
| Data Structure| Operation | Time Complexity |
|---|---|---|

| Array | Access | O(1) |
|  | Insertion/Deletion | O(n) |

| Stack | Push/Pop | O(1) |

| Queue | Enqueue/Dequeue | O(1) |

| Linked List | Insertion/Deletion (at head) | O(1) |
|  | Access (by index) | O(n) |
