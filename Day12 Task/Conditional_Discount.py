# 4. Conditional Discount System (List Comprehension)
# A shop has prices:
# prices = [100, 200, 300, 400]
# Scenario:
# ● Apply a 10% discount only if price > 200.
# Task:
# ● Use list comprehension with condition to create updated price list.

# Solution
prices = [100, 200, 300, 400]

# if price > 200 -> 10% off (90% of price), else keep the same price
updated = [p * 0.9 if p > 200 else p for p in prices]
print(updated)     # [100, 200, 270.0, 360.0]
