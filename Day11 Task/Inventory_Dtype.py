# 6. Check Data Type of Inventory Values
# A warehouse stores product quantities:
# [10, 20, 30, 40]
# Task:
# ● Convert it into a NumPy array.
# ● Print the data type (dtype) of the array.

# Solution
import numpy as np

qty = np.array([10, 20, 30, 40])
print(qty.dtype)       # int64 -> all values are integers
