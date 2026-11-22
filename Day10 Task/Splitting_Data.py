#Splitting Data for Parallel Processing
""" Data = [5, 10, 15, 20, 25, 30]
 Task: Store in an array and split into 3 equal parts."""

import numpy as np
#Store the data in an array.
data = np.array([5, 10, 15, 20, 25, 30])
#np.split(array, 3) divides into 3 equal parts (6 items / 3 = 2 each).
parts = np.split(data, 3)
print("Split into 3 parts:", parts)   # [array([ 5, 10]), array([15, 20]), array([25, 30])]
