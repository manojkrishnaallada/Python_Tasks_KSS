# 10. Data Cleaning + Visualization
# Scenario:
# data = np.array([100, np.nan, 200, 150, np.nan, 300])
# Task:
# 1. Convert to Pandas Series
# 2. Replace NaN with mean
# 3. Plot:
# ○ Line graph of cleaned data
# ○ Bar chart of values > average

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

# 1. Convert to Pandas Series
series = pd.Series(data)
print("Before cleaning:")
print(series)

# 2. Replace NaN with mean (mean() ignores NaN values automatically)
mean_value = series.mean()
series = series.fillna(mean_value)
print("After cleaning:")
print(series)

# Average of cleaned data
average = series.mean()

# Values greater than average
above_avg = series[series > average]

# 3. Plot both graphs in one figure
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Line graph of cleaned data
axes[0].plot(series, marker="o")
axes[0].set_title("Cleaned Data")

# Bar chart of values > average
axes[1].bar(above_avg.index, above_avg.values)
axes[1].set_title("Values > Average")

plt.tight_layout()
plt.show()
