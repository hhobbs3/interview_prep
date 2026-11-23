"""
Numpy Demo / Cheatsheet
======================

This file is a lightweight reference that shows the *core* features of
`numpy` – the ubiquitous numerical‑array library for Python.  It is
intended as a quick‑start guide for people who have never used
`numpy` before, or who need a quick reminder of the most common
operations.

The examples are small, self‑contained, and include plenty of comments
so you can see why each line is there.  Feel free to copy, modify or
extend the demo for your own projects.

Typical workflow
----------------
1. Import :mod:`numpy` as ``np``.
2. Create arrays (``np.array``, ``np.arange``, ``np.zeros`` …).
3. Index / slice the array.
4. Perform arithmetic / broadcasting.
5. Use universal functions (ufuncs) like ``np.sin`` or ``np.exp``.
6. Run simple statistics: mean, sum, std, etc.
7. (Optional) reshape or view arrays.

Run this script directly with ``python numpy_demo.py``.  The output
will demonstrate the results of each section.
"""


# ---------------------------------------------------------------------------
# 1. Imports
# ---------------------------------------------------------------------------
import numpy as np


# ---------------------------------------------------------------------------
# 2. Creating arrays
# ---------------------------------------------------------------------------
# 2.1 1‑D array from a Python list
arr1 = np.array([1, 2, 3, 4])
print("arr1 (1‑D):", arr1)

# 2.2 2‑D array from a nested list
arr2 = np.array([[1, 2], [3, 4]])
print("arr2 (2‑D):\n", arr2)

# 2.3 Sequence helpers
#   - arange: like range, but returns an array
#   - linspace: creates evenly spaced values in an interval
print("np.arange(0, 5):", np.arange(0, 5))
print("np.linspace(0, 1, 5):", np.linspace(0, 1, 5))

# 2.4 Special value arrays
print("np.zeros((2,3)):\n", np.zeros((2, 3)))
print("np.ones((2,3)):\n", np.ones((2, 3)))
print("np.eye(3) (identity matrix):\n", np.eye(3))


# ---------------------------------------------------------------------------
# 3. Indexing & Slicing
# ---------------------------------------------------------------------------
# 3.1 Single element access
print("arr2[0, 1] (first row, second column):", arr2[0, 1])

# 3.2 Slice: row 1 (index 1) across all columns
print("arr2[1, :] (second row):", arr2[1, :])

# 3.3 Slice: all rows, column 0
print("arr2[:, 0] (first column):", arr2[:, 0])

# 3.4 Negative indices count from the end
print("arr2[-1, -1] (bottom‑right):", arr2[-1, -1])

# 3.5 Fancy indexing: choose arbitrary indices
rows = np.array([0, 1])
cols = np.array([1, 0])
print("fancy indexing arr2[[0,1], [1,0]]: ", arr2[rows, cols])


# ---------------------------------------------------------------------------
# 4. Basic arithmetic & broadcasting
# ---------------------------------------------------------------------------
# 4.1 Element‑wise operations
print("arr1 + 10:", arr1 + 10)
print("arr1 * 2:", arr1 * 2)

# 4.2 Broadcasting: add a scalar or a 1‑D array
arr3 = np.array([10, 20, 30, 40])
print("arr1 + arr3 (element‑wise):", arr1 + arr3)

# 4.3 Shape mismatch handled by broadcasting
mat = np.array([[1, 2, 3], [4, 5, 6]])
print("mat + [10, 20, 30]:", mat + np.array([10, 20, 30]))


# ---------------------------------------------------------------------------
# 5. Universal functions (ufuncs)
# ---------------------------------------------------------------------------
# 5.1 Trigonometric & exponential
print("np.sin(arr1):", np.sin(arr1))
print("np.exp(arr1):", np.exp(arr1))

# 5.2 Aggregating with ufuncs
print("np.maximum(arr1, arr3):", np.maximum(arr1, arr3))
print("np.sqrt(arr3):", np.sqrt(arr3))


# ---------------------------------------------------------------------------
# 6. Statistics & aggregation
# ---------------------------------------------------------------------------
print("arr1.mean():", arr1.mean())
print("arr3.std():", arr3.std())
print("mat.sum():", mat.sum())
print("mat.cumsum():", mat.cumsum())

# 6.1 Along an axis
print("mat.sum(axis=0) (sum of columns):", mat.sum(axis=0))
print("mat.sum(axis=1) (sum of rows):", mat.sum(axis=1))


# ---------------------------------------------------------------------------
# 7. Reshaping & viewing
# ---------------------------------------------------------------------------
# 7.1 Reshape a flat array into a matrix
flat = np.arange(12)
reshaped = flat.reshape((3, 4))
print("reshaped (3x4):\n", reshaped)

# 7.2 View (no copy, just different shape)
view = reshaped[1:, :2]
print("view of reshaped (sub‑array):\n", view)

# 7.3 Transpose
print("reshaped.T (transpose):\n", reshaped.T)


# ---------------------------------------------------------------------------
# 8. Random numbers
# ---------------------------------------------------------------------------
print("np.random.rand(2,3) (uniform in [0,1)):", np.random.rand(2, 3))
print("np.random.randn(2,3) (normal distribution):", np.random.randn(2, 3))


# ---------------------------------------------------------------------------
# End of demo
# ---------------------------------------------------------------------------
print("\nDemo complete.  Feel free to experiment with the code above!")

"""
# ---------------------------------------------------------------------------
# If you run this file directly, it will execute the demo.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    pass  # The code above runs on import
"""
if __name__ == "__main__":
    pass  # The code above runs on import
