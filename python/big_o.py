"""Examples of functions demonstrating common Big O complexities.

Each function is intentionally simple and focuses on the algorithmic pattern
that gives it its time complexity.
"""

import math

# O(1) – constant time

def constant_time() -> int:
    """Return a constant value. Execution time does not depend on input size.
    Complexity: O(1)"""
    return 42

# O(log n) – logarithmic time (binary search style)

def logarithmic_time(n: int) -> int:
    """Return the number of times we can divide ``n`` by 2 until it reaches 1.
    Complexity: O(log n)"""
    count = 0
    while n > 1:
        n //= 2 # floor division to ensure we stay in integer domain
        count += 1
    return count

# O(n) – linear time

def linear_time(arr: list[int]) -> int:
    """Return the sum of all elements in ``arr``.
    Complexity: O(n)"""
    total = 0
    for x in arr:
        total += x
    return total

# O(n log n) – linearithmic time (sorting)

def linearithmic_time(arr: list[int]) -> list[int]:
    """Return a new list containing the sorted elements of ``arr``.
    Complexity: O(n log n)"""
    return sorted(arr)

# O(n log n) – linearithmic time (merge sort)

def merge_sort(arr: list[int]) -> list[int]:
    """Return a sorted copy of ``arr`` using merge sort.
    Complexity: O(n log n) because the list is repeatedly divided in half
    (log n levels) and each level performs O(n) merging work.
    """
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# O(n²) – quadratic time

def quadratic_time(arr: list[int]) -> int:
    """Return the sum of all pairwise products in ``arr``.
    Complexity: O(n^2)"""
    total = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            total += arr[i] * arr[j]
    return total

# O(n³) – cubic time

def cubic_time(arr: list[int]) -> int:
    """Return the sum of all triplewise products in ``arr``.
    Complexity: O(n^3)"""
    total = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += arr[i] * arr[j] * arr[k]
    return total

# O(2^n) – exponential time (simple recursion)

def exponential_time(n: int) -> int:
    """Return the n-th Fibonacci number using a naive recursive algorithm.
    Complexity: O(2^n)"""
    if n <= 1:
        return n
    return exponential_time(n - 1) + exponential_time(n - 2)

# O(n!) – factorial time (permutations)

def factorial_time(arr: list[int]) -> list[tuple[int, ...]]:
    """Return all permutations of ``arr``.
    Complexity: O(n!)"""
    if len(arr) == 0:
        return [()]
    permutations = []
    for i, value in enumerate(arr):
        rest = arr[:i] + arr[i + 1 :]
        for p in factorial_time(rest):
            permutations.append((value,) + p)
    return permutations

# A quick test suite – not part of the big O examples, but handy for manual checks.
if __name__ == "__main__":
    print("constant_time() ->", constant_time())
    print("logarithmic_time(1024) ->", logarithmic_time(1024))
    print("linear_time([1,2,3]) ->", linear_time([1, 2, 3]))
    print("linearithmic_time([3,1,2]) ->", linearithmic_time([3, 1, 2]))
    print("quadratic_time([1,2]) ->", quadratic_time([1, 2]))
    print("cubic_time([1,2]) ->", cubic_time([1, 2]))
    print("exponential_time(5) ->", exponential_time(5))
    print("factorial_time([1,2,3]) ->", factorial_time([1, 2, 3]))
