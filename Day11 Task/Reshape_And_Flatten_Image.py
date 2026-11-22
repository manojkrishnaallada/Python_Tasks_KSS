# 15. Reshape and Flatten Image Data
# Scenario:
# An image is stored as a 2 × 3 matrix:
# [[1,2,3],
# [4,5,6]]
# Task:
# 1. Convert it into a NumPy array.
# 2. Flatten the array into 1-D format.
# 3. Print the flattened array.

# Solution
import numpy as np

image = np.array([[1, 2, 3],
                  [4, 5, 6]])          # 1. 2x3 array
flat = image.flatten()                 # 2. 2-D -> 1-D
print(flat)                            # 3. [1 2 3 4 5 6]
