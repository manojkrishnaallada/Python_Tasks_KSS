# 7. Convert Float Prices to Integer
# A shop stores product prices:
# [10.5, 20.8, 15.3]
# Scenario:
# The billing system requires integer values.
# Task:
# ● Convert the array from float to integer using astype().

# Solution
import numpy as np

prices = np.array([10.5, 20.8, 15.3])
int_prices = prices.astype(int)     # float -> int (decimal part is cut off)
print(int_prices)                   # [10 20 15]
