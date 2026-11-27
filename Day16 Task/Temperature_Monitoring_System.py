# 4. Temperature Monitoring System
# Scenario:
# temps = np.array([28, 30, 32, 35, 33, 31, 29])
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# Task:
# ● Create DataFrame
# ● Plot:
# ○ Line graph → daily temperature trend
# ○ Bar chart → day-wise temperature
# ○ Pie chart → proportion of high (>30) vs low temps
# ○ Histogram → temperature frequency
# ○ Scatter plot → day index vs temperature

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Create DataFrame
df = pd.DataFrame({"Day": days, "Temp": temps})
print(df)

fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# Line graph -> daily temperature trend
axes[0, 0].plot(df["Day"], df["Temp"], marker="o")
axes[0, 0].set_title("Line Graph - Daily Temperature")

# Bar chart -> day-wise temperature
axes[0, 1].bar(df["Day"], df["Temp"])
axes[0, 1].set_title("Bar Chart - Day-wise Temperature")

# Pie chart -> proportion of high (>30) vs low temps
high = (df["Temp"] > 30).sum()
low = (df["Temp"] <= 30).sum()
axes[0, 2].pie([high, low], labels=["High (>30)", "Low (<=30)"], autopct="%1.1f%%")
axes[0, 2].set_title("Pie Chart - High vs Low")

# Histogram -> temperature frequency
axes[1, 0].hist(df["Temp"], bins=5, edgecolor="black")
axes[1, 0].set_title("Histogram - Temperature Frequency")

# Scatter plot -> day index vs temperature
axes[1, 1].scatter(df.index, df["Temp"])
axes[1, 1].set_title("Scatter Plot - Day Index vs Temp")

axes[1, 2].axis("off")

plt.tight_layout()
plt.show()
