# 10. Random Matrix and Condition Filtering
# Scenario:
# ● Generate a 3×3 matrix of random numbers (0–50).
# Task:
# ● Filter elements greater than 25.
# ● Print filtered values.

# Solution
import numpy as np

matrix = np.random.randint(0, 51, (3, 3))    # 3x3 matrix, values 0 to 50
print(matrix)
print(matrix[matrix > 25])                   # only values greater than 25
