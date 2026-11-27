# 3. Expense Distribution Pie Chart
# Scenario:
# Monthly expenses:
# expenses = np.array([500, 300, 200])
# labels = ["Food", "Rent", "Travel"]
# Task:
# ● Create a pie chart
# ● Show percentage distribution

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]

# Create a pie chart; autopct shows the percentage on each slice
plt.pie(expenses, labels=labels, autopct="%1.1f%%")
plt.title("Expense Distribution")
plt.show()
