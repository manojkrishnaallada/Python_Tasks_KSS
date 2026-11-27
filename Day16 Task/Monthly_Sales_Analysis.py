# 2. Monthly Sales Analysis
# Scenario:
# sales = np.array([100, 150, 200, 180, 220, 300])
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# Task:
# ● Create DataFrame
# ● Plot:
# ○ Line graph → sales trend
# ○ Bar chart → month-wise comparison
# ○ Pie chart → contribution of each month
# ○ Histogram → frequency of sales values
# ○ Scatter plot → month index vs sales

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Create DataFrame
df = pd.DataFrame({"Month": months, "Sales": sales})
print(df)

fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# Line graph -> sales trend
axes[0, 0].plot(df["Month"], df["Sales"], marker="o")
axes[0, 0].set_title("Line Graph - Sales Trend")

# Bar chart -> month-wise comparison
axes[0, 1].bar(df["Month"], df["Sales"])
axes[0, 1].set_title("Bar Chart - Month-wise Sales")

# Pie chart -> contribution of each month
axes[0, 2].pie(df["Sales"], labels=df["Month"], autopct="%1.1f%%")
axes[0, 2].set_title("Pie Chart - Contribution of Each Month")

# Histogram -> frequency of sales values
axes[1, 0].hist(df["Sales"], bins=5, edgecolor="black")
axes[1, 0].set_title("Histogram - Sales Frequency")

# Scatter plot -> month index vs sales
axes[1, 1].scatter(df.index, df["Sales"])
axes[1, 1].set_title("Scatter Plot - Month Index vs Sales")

axes[1, 2].axis("off")

plt.tight_layout()
plt.show()
