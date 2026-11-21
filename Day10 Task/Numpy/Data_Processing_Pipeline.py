# Data Processing Pipeline
""" Array = [12, 7, 25, 3, 18, 10]
 Task: Convert to array, sort, split into two equal parts
        and find the sum of each part."""

import numpy as np
#Convert the list into a NumPy array.
pipeline = np.array([12, 7, 25, 3, 18, 10])
#Sort ascending.
sorted_arr = np.sort(pipeline)
#Split the sorted array into 2 equal parts (3 items each).
part1, part2 = np.split(sorted_arr, 2)
#Sum each part.
print("Sorted array:", sorted_arr)        # [ 3  7 10 12 18 25]
print("Part 1:", part1, "-> Sum:", part1.sum())  # [ 3  7 10] -> 20
print("Part 2:", part2, "-> Sum:", part2.sum())  # [12 18 25] -> 55


