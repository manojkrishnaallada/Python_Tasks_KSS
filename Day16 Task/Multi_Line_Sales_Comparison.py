# 6. Multi-Line Graph for Sales Comparison
# Scenario:
# data = {
# "Month": ["Jan", "Feb", "Mar"],
# "Store_A": [100, 150, 200],
# "Store_B": [90, 140, 210]
# }
# Task:
# ● Create DataFrame
# ● Plot two line graphs on same plot
# ● Add legend

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A": [100, 150, 200],
    "Store_B": [90, 140, 210]
}

# Create DataFrame
df = pd.DataFrame(data)
print(df)

# Plot two line graphs on same plot (label is used by the legend)
plt.plot(df["Month"], df["Store_A"], marker="o", label="Store A")
plt.plot(df["Month"], df["Store_B"], marker="s", label="Store B")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Comparison")

# Add legend
plt.legend()
plt.show()
