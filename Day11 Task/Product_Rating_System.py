# 3. Product Rating System
# An e-commerce website stores product ratings:
# [4, 5, 3, 4, 2]
# Task:
# ● Convert it to a NumPy array.
# ● Print the first and last rating using indexing.

# Solution
import numpy as np

ratings = np.array([4, 5, 3, 4, 2])
print(ratings[0])      # first rating (index starts at 0)
print(ratings[-1])     # last rating (-1 counts from the end)
