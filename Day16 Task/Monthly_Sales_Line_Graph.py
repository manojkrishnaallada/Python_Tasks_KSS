# 1. Monthly Sales Line Graph
# Scenario:
# A shop records monthly sales:
# sales = np.array([100, 150, 200, 250, 300])
# months = ["Jan", "Feb", "Mar", "Apr", "May"]
# Task:
# ● Convert data into a Pandas DataFrame
# ● Plot a line graph
# ● Label X-axis as months and Y-axis as sales

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]

# Convert data into a Pandas DataFrame
df = pd.DataFrame({"Month": months, "Sales": sales})
print(df)

# Plot a line graph
plt.plot(df["Month"], df["Sales"], marker="o")

# Label X-axis as months and Y-axis as sales
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()
