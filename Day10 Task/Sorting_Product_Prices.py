# Sorting Product Prices

""" Prices = [499, 299, 799, 199, 599]
 Task: Convert to a NumPy array and sort in ascending order."""

import numpy as np
#Convert the list to an array.
prices = np.array([499, 299, 799, 199, 599])
#np.sort() returns a new sorted array (ascending by default).
sorted_prices = np.sort(prices)
print("Sorted prices:", sorted_prices)   # [199 299 499 599 799]
