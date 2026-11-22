# 10. Find Indexes of Specific Value
# A quality check system stores product defect codes:
# [2, 4, 1, 4, 3, 4, 5]
# Task:
# ● Find the indexes where value = 4 using NumPy searching.

# Solution
import numpy as np

codes = np.array([2, 4, 1, 4, 3, 4, 5])
print(np.where(codes == 4)[0])     # indexes where condition is True -> [1 3 5]
