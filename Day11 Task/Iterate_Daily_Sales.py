# 8. Iterate Through Daily Sales
# Daily sales data:
# [200, 300, 150, 400]
# Task:
# ● Store it in a NumPy array.
# ● Iterate through the array and print each sale value.

# Solution
import numpy as np

sales = np.array([200, 300, 150, 400])
for sale in sales:       # each loop gives one element
    print(sale)
