# 11. Filter High Temperature Values
# A weather station records temperatures:
# [28, 31, 35, 27, 40, 22]
# Scenario:
# The system needs temperatures above 30°C.
# Task:
# ● Filter the values greater than 30 using NumPy boolean filtering.

# Solution
import numpy as np

temps = np.array([28, 31, 35, 27, 40, 22])
mask = temps > 30          # True/False for each value
print(temps[mask])         # only True positions -> [31 35 40]
