# 11. Boolean Masking for Salary Analysis
# Scenario:
# Employee salaries:
# [25000, 40000, 15000, 50000, 30000]
# Task:
# ● Filter salaries above 30000.
# ● Count how many employees satisfy this condition.

# Solution
import numpy as np

salaries = np.array([25000, 40000, 15000, 50000, 30000])
high = salaries[salaries > 30000]      # boolean masking
print(high)                            # [40000 50000]
print(len(high))                       # 2 -> number of employees
