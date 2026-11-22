# 5. Accessing Matrix Data
# A teacher stores marks of students in two subjects:
# [[78, 85],
# [90, 88],
# [67, 72]]
# Task:
# ● Convert it to a NumPy array.
# ● Access the second student's second subject mark.

# Solution
import numpy as np

marks = np.array([[78, 85],
                  [90, 88],
                  [67, 72]])
print(marks[1, 1])     # [row, column] -> 2nd student = row 1, 2nd subject = column 1
