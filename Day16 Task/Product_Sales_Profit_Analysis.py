# 5. Product Sales & Profit Analysis
# Scenario:
# sales = np.array([200, 300, 250, 400, 350])
# profit = np.array([50, 70, 60, 90, 80])
# products = ["A", "B", "C", "D", "E"]
# Task:
# ● Create DataFrame
# ● Plot:
# ○ Line graph → sales trend
# ○ Bar chart → product vs sales
# ○ Pie chart → sales contribution
# ○ Histogram → profit distribution
# ○ Scatter plot → sales vs profit

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

# Create DataFrame
df = pd.DataFrame({"Product": products, "Sales": sales, "Profit": profit})
print(df)

fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# Line graph -> sales trend
axes[0, 0].plot(df["Product"], df["Sales"], marker="o")
axes[0, 0].set_title("Line Graph - Sales Trend")

# Bar chart -> product vs sales
axes[0, 1].bar(df["Product"], df["Sales"])
axes[0, 1].set_title("Bar Chart - Product vs Sales")

# Pie chart -> sales contribution
axes[0, 2].pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")
axes[0, 2].set_title("Pie Chart - Sales Contribution")

# Histogram -> profit distribution
axes[1, 0].hist(df["Profit"], bins=5, edgecolor="black")
axes[1, 0].set_title("Histogram - Profit Distribution")

# Scatter plot -> sales vs profit
axes[1, 1].scatter(df["Sales"], df["Profit"])
axes[1, 1].set_xlabel("Sales")
axes[1, 1].set_ylabel("Profit")
axes[1, 1].set_title("Scatter Plot - Sales vs Profit")

axes[1, 2].axis("off")

plt.tight_layout()
plt.show()
