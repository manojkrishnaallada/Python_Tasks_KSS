# 6. Multi-Level List Transformation (Advanced List Comprehension)
# A dataset contains:
# data = [[1, 2, 3], [4, 5], [6]]
# Task:
# ● Flatten the list using list comprehension.
# ● Then create a new list containing squares of only even numbers.

# Solution
data = [[1, 2, 3], [4, 5], [6]]

flat = [x for sub in data for x in sub]       # outer loop: each sublist, inner loop: each item
print(flat)                                   # [1, 2, 3, 4, 5, 6]

squares = [x ** 2 for x in flat if x % 2 == 0]   # only even numbers, squared
print(squares)                                # [4, 16, 36]
