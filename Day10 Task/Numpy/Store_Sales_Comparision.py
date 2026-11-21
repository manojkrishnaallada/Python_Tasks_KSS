# Store Sales Comparison
""" Store A = [200, 250, 300]   Store B = [180, 270, 310]
 Task: Store in arrays, find daily difference, print result."""

import numpy as np
#Store each store's sales in an array.
store_a = np.array([200, 250, 300])
store_b = np.array([180, 270, 310])
#Subtracting arrays works element by element (day by day).
difference = store_a - store_b
print("Daily difference (A - B):", difference)   # [ 20 -20 -10]

 
