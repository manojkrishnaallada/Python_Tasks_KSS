# 4. Temperature Trend Line Plot
# Scenario:
# Daily temperatures:
# temps = np.array([28, 30, 32, 31, 29])
# Task:
# ● Convert into Pandas Series
# ● Plot a line graph
# ● Add title and grid

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 31, 29])

# Convert into Pandas Series
series = pd.Series(temps)
print(series)

# Plot a line graph
plt.plot(series, marker="o")

# Add title and grid
plt.title("Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()
