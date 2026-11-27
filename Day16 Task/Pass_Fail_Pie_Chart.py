# 8. Pie Chart with Conditional Data
# Scenario:
# scores = np.array([40, 60, 80, 30, 90])
# Task:
# ● Categorize into:
# ○ Pass (>50)
# ○ Fail (<=50)
# ● Count using NumPy/Pandas
# ● Plot pie chart for Pass vs Fail

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores = np.array([40, 60, 80, 30, 90])

# Categorize and count using NumPy
# (scores > 50 gives True/False values; sum counts the True ones)
pass_count = np.sum(scores > 50)
fail_count = np.sum(scores <= 50)
print("Pass:", pass_count)
print("Fail:", fail_count)

# Plot pie chart for Pass vs Fail
plt.pie([pass_count, fail_count], labels=["Pass", "Fail"], autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()
