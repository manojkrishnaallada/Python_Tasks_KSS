# 7. Filtered Bar Chart
# Scenario:
# marks = np.array([45, 80, 60, 30, 90])
# names = ["A", "B", "C", "D", "E"]
# Task:
# ● Convert to DataFrame
# ● Filter students with marks > 50
# ● Plot bar chart only for filtered students

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

# Convert to DataFrame
df = pd.DataFrame({"Name": names, "Marks": marks})

# Filter students with marks > 50
filtered = df[df["Marks"] > 50]
print(filtered)

# Plot bar chart only for filtered students
plt.bar(filtered["Name"], filtered["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students with Marks > 50")
plt.show()
