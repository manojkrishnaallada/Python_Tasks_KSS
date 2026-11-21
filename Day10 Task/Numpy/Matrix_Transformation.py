# Matrix Transformation in Image Processing
""" Matrix = [[1, 2], [3, 4]]
 Task: Create the array, find its transpose, print both."""

import numpy as np
#Create the 2x2 matrix.
matrix = np.array([[1, 2],
                   [3, 4]])
#.T swaps rows and columns (np.transpose(matrix) also works).
transpose = matrix.T
print("Original:\n", matrix)
print("Transpose:\n", transpose)   # [[1 3] [2 4]]
