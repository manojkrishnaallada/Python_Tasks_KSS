# 4. Student Roll Numbers Extraction
# A list contains roll numbers:
# [101, 102, 103, 104, 105, 106]
# Scenario:
# You want only the middle students (index 2 to 4).
# Task:
# ● Use NumPy slicing to extract those values.

# Solution
import numpy as np

rolls = np.array([101, 102, 103, 104, 105, 106])
print(rolls[2:5])      # [start:end] -> end excluded, so 2:5 gives index 2,3,4
