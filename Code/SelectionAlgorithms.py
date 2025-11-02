import random
import time
import statistics
from typing import List, Tuple


# -------------------------------------------------
# Deterministic Selection (Median of Medians)
# -------------------------------------------------

def partition_around_pivot(arr: List[int], pivot_value: int) -> Tuple[int, int]:
    """3-way partition: returns indices delimiting pivot region."""
    lt, i, gt = 0, 0, len(arr)
    while i < gt:
        if arr[i] < pivot_value:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot_value:
            gt -= 1
            arr[i], arr[gt] = arr[gt], arr[i]
        else:
            i += 1
    return lt, gt


def deterministic_select(arr: List[int], k: int) -> int:
    """Selects the k-th smallest element using Median of Medians."""
    if not 0 <= k < len(arr):
        raise IndexError("k out of range")

    def select(a: List[int], k: int) -> int:
        if len(a) <= 10:
            a.sort()
            return a[k]

        # 1. Divide into groups of 5 and find medians
        medians = []
        for i in range(0, len(a), 5):
            group = sorted(a[i:i+5])
            medians.append(group[len(group)//2])

        # 2. Find median of medians
        pivot = select(medians, len(medians)//2)

        # 3. Partition around pivot
        left_end, right_start = partition_around_pivot(a, pivot)

        # 4. Recursive case
        if k < left_end:
            return select(a[:left_end], k)
        elif k < right_start:
            return pivot
        else:
            return select(a[right_start:], k - right_start)

    return select(list(arr), k)


# -------------------------------------------------
# Randomized Selection (Quickselect)
# -------------------------------------------------

def randomized_select(arr: List[int], k: int) -> int:
    """Expected O(n) selection using random pivot (Quickselect)."""
    if not 0 <= k < len(arr):
        raise IndexError("k out of range")

    def select(a: List[int], k: int) -> int:
        while True:
            if len(a) <= 10:
                a.sort()
                return a[k]
            pivot = random.choice(a)
            left_end, right_start = partition_around_pivot(a, pivot)
            if k < left_end:
                a = a[:left_end]
            elif k < right_start:
                return pivot
            else:
                a = a[right_start:]
                k -= right_start

    return select(list(arr), k)


# -------------------------------------------------
# Empirical Analysis
# -------------------------------------------------

def make_array(n: int, kind: str = "random"):
    """Generate arrays of different distributions."""
    if kind == "random":
        return [random.randint(0, n*10) for _ in range(n)]
    elif kind == "sorted":
        return list(range(n))
    elif kind == "reversed":
        return list(range(n, 0, -1))
    elif kind == "duplicates":
        return [random.randint(0, 10) for _ in range(n)]
    else:
        raise ValueError("Invalid kind")


def benchmark_selection():
    print("\n=== Benchmark: Deterministic vs Randomized Selection ===")
    sizes = [1000, 5000, 10000]
    distributions = ["random", "sorted", "reversed", "duplicates"]

    for n in sizes:
        print(f"\nInput size: {n}")
        for dist in distributions:
            arr = make_array(n, dist)
            k = n // 2

            start = time.perf_counter()
            deterministic_select(arr, k)
            det_time = (time.perf_counter() - start) * 1000

            start = time.perf_counter()
            randomized_select(arr, k)
            rand_time = (time.perf_counter() - start) * 1000

            print(f"{dist:>10} | Deterministic: {det_time:8.2f} ms | Randomized: {rand_time:8.2f} ms")

    print("\nBenchmark completed.")

# -------------------------------------------------
# Run if executed directly
# -------------------------------------------------
if __name__ == "__main__":
    random.seed(42)
    benchmark_selection()
