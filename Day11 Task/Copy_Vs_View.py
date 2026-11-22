# 13. Copy vs View Behavior in Data Processing
# Scenario:
# A dataset:
# [10, 20, 30, 40]
# Task:
# ● Create a copy of the array.
# ● Modify the original array.
# ● Show that the copy does not change.
# ● Repeat using view() and observe the difference.

# Solution
import numpy as np

# ---- Copy ----
arr = np.array([10, 20, 30, 40])
c = arr.copy()         # new independent array
arr[0] = 99            # modify original
print(arr)             # [99 20 30 40]
print(c)               # [10 20 30 40] -> copy does not change

# ---- View ----
arr = np.array([10, 20, 30, 40])
v = arr.view()         # shares the same data as original
arr[0] = 99            # modify original
print(arr)             # [99 20 30 40]
print(v)               # [99 20 30 40] -> view also changes
