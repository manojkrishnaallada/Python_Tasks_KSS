# 9. Combined Visualization Dashboard
# Scenario:
# sales = np.array([100, 200, 150, 300])
# products = ["A", "B", "C", "D"]
# Task:
# ● Create DataFrame
# ● Plot:
# ○ Line graph (trend)
# ○ Bar chart (comparison)
# ○ Pie chart (distribution)
# ● Show all in single figure (subplots)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

# Create DataFrame
df = pd.DataFrame({"Product": products, "Sales": sales})
print(df)

# One figure with 3 plots side by side (1 row, 3 columns)
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Line graph (trend)
axes[0].plot(df["Product"], df["Sales"], marker="o")
axes[0].set_title("Line Graph - Trend")

# Bar chart (comparison)
axes[1].bar(df["Product"], df["Sales"])
axes[1].set_title("Bar Chart - Comparison")

# Pie chart (distribution)
axes[2].pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")
axes[2].set_title("Pie Chart - Distribution")

plt.tight_layout()
plt.show()
