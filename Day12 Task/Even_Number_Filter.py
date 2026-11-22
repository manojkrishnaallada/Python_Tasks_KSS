# 2. Even Number Filter (List Comprehension)
# A system stores numbers:
# nums = [1, 2, 3, 4, 5, 6]
# Task:
# ● Use list comprehension to create a new list containing only even numbers.

# Solution
nums = [1, 2, 3, 4, 5, 6]

evens = [n for n in nums if n % 2 == 0]    # keep n only if divisible by 2
print(evens)                               # [2, 4, 6]
