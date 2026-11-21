# Multi-Department Data Aggregation
""" Branch A = [[10, 20], [30, 40]]   Branch B = [[5, 15], [25, 35]]
  Task: Combine the matrices, find total employees, print both."""

import numpy as np
#Create both branch matrices.
branch_a = np.array([[10, 20], [30, 40]])
branch_b = np.array([[5, 15], [25, 35]])
#np.vstack() stacks Branch B below Branch A (4 rows x 2 columns).
combined_matrix = np.vstack((branch_a, branch_b))
#np.sum() adds every element of the combined matrix.
total = np.sum(combined_matrix)
print("Combined matrix:\n", combined_matrix)
print("Total employees:", total)   # 180
 
