# 1. Bank Transaction Storage
# A bank stores the transaction amounts of a customer in a list:
# [1200, 500, 800, 1500]
# Scenario:
# ● Convert the list into a NumPy array.
# ● Print the type of the object.
# ● Verify that it is a NumPy ndarray.

# Solution
import numpy as np

transactions = [1200, 500, 800, 1500]
arr = np.array(transactions)          # list -> NumPy array
print(arr)
print(type(arr))                      # <class 'numpy.ndarray'>
print(isinstance(arr, np.ndarray))    # True -> it is an ndarray
