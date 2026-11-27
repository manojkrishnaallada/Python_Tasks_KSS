# 1. Student Performance Dashboard
# Scenario:
# A school records marks of students in one subject:
# marks = np.array([45, 67, 89, 56, 72, 91, 38])
# students = ["A", "B", "C", "D", "E", "F", "G"]
# Task:
# ● Convert to Pandas DataFrame
# ● Plot:
# ○ Line graph → trend of marks
# ○ Bar chart → student vs marks
# ○ Pie chart → Pass (>50) vs Fail
# ○ Histogram → distribution of marks
# ○ Scatter plot → index vs marks

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

# Convert to Pandas DataFrame
df = pd.DataFrame({"Student": students, "Marks": marks})
print(df)

# One figure with 2 rows x 3 columns of plots
fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# Line graph -> trend of marks
axes[0, 0].plot(df["Student"], df["Marks"], marker="o")
axes[0, 0].set_title("Line Graph - Trend of Marks")

# Bar chart -> student vs marks
axes[0, 1].bar(df["Student"], df["Marks"])
axes[0, 1].set_title("Bar Chart - Student vs Marks")

# Pie chart -> Pass (>50) vs Fail
passed = (df["Marks"] > 50).sum()
failed = (df["Marks"] <= 50).sum()
axes[0, 2].pie([passed, failed], labels=["Pass", "Fail"], autopct="%1.1f%%")
axes[0, 2].set_title("Pie Chart - Pass vs Fail")

# Histogram -> distribution of marks
axes[1, 0].hist(df["Marks"], bins=5, edgecolor="black")
axes[1, 0].set_title("Histogram - Distribution of Marks")

# Scatter plot -> index vs marks
axes[1, 1].scatter(df.index, df["Marks"])
axes[1, 1].set_title("Scatter Plot - Index vs Marks")

# Last box is empty, so hide it
axes[1, 2].axis("off")

plt.tight_layout()
plt.show()
