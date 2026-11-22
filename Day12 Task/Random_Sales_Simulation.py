# 8. Random Sales Simulation
# Scenario:
# A company wants to simulate 10 days of sales (range 100–500).
# Task:
# ● Generate random integers using NumPy.
# ● Print the array.
# ● Find the average sales.

# Solution
import numpy as np

sales = np.random.randint(100, 501, 10)    # 10 numbers from 100 to 500 (501 excluded)
print(sales)
print(np.mean(sales))                      # average sales
