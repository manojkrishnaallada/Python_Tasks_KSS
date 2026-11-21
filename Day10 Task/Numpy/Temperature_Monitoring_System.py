# Temperature Monitoring System
""" Day 1: [30, 32, 31]   Day 2: [29, 33, 34]
 Task: Create a 2D array, print it, find the total temperature."""

import numpy as np

#Pass a list of lists to np.array() -> 2D array (2 rows, 3 columns).
temps = np.array([[30, 32, 31], [29, 33, 34]])
# Print the array.
print("Temperatures:\n", temps)
#np.sum() without an axis adds up ALL elements.
print("Total temperature:", np.sum(temps))   # 189
