# Part 1: Implementation and Analysis of Selection Algorithms

## Overview
This project focuses on the implementation and performance analysis of algorithms for finding the **k-th smallest element** in an array, also known as **order statistics**. It includes both the **deterministic Median of Medians algorithm** (guaranteed worst-case linear time) and the **randomized Quickselect algorithm** (expected linear time).  

The study compares their theoretical complexities and empirical performance across different input distributions.

---

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
