# 3. Employee Salary Insights
# Scenario:
# salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
# departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
# Task:
# ● Convert into DataFrame
# ● Plot:
# ○ Line graph → salary trend
# ○ Bar chart → department-wise salary comparison
# ○ Pie chart → department distribution
# ○ Histogram → salary distribution
# ○ Scatter plot → index vs salary

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

# Convert into DataFrame
df = pd.DataFrame({"Department": departments, "Salary": salaries})
print(df)

# Average salary of each department (for the bar chart)
dept_salary = df.groupby("Department")["Salary"].mean()

# Number of employees in each department (for the pie chart)
dept_count = df["Department"].value_counts()

fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# Line graph -> salary trend
axes[0, 0].plot(df["Salary"], marker="o")
axes[0, 0].set_title("Line Graph - Salary Trend")

# Bar chart -> department-wise salary comparison
axes[0, 1].bar(dept_salary.index, dept_salary.values)
axes[0, 1].set_title("Bar Chart - Avg Salary by Department")

# Pie chart -> department distribution
axes[0, 2].pie(dept_count.values, labels=dept_count.index, autopct="%1.1f%%")
axes[0, 2].set_title("Pie Chart - Department Distribution")

# Histogram -> salary distribution
axes[1, 0].hist(df["Salary"], bins=5, edgecolor="black")
axes[1, 0].set_title("Histogram - Salary Distribution")

# Scatter plot -> index vs salary
axes[1, 1].scatter(df.index, df["Salary"])
axes[1, 1].set_title("Scatter Plot - Index vs Salary")

axes[1, 2].axis("off")

plt.tight_layout()
plt.show()
