# Student Marks Analysis
""" Marks = [45, 67, 89, 56, 72]
  Task: Convert the list into a NumPy array, add 5 grace marks to every student, print the updated marks."""

import numpy as np

#Create a Python list of marks.
marks = [45, 67, 89, 56, 72]
#Convert the list into a NumPy array with np.array().
marks_arr = np.array(marks)
#Adding a number to an array adds it to EVERY element (broadcasting).
marks_arr = marks_arr + 5
#Print the result.
print("Updated marks:", marks_arr)   # [50 72 94 61 77]
