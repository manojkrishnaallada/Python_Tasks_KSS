# 12. Random Dataset Normalization + Filtering
# Scenario:
# ● Generate 8 random float values between 0 and 1.
# Task:
# 1. Normalize by multiplying with 100
# 2. Filter values greater than 50
# 3. Sort the filtered values

# Solution
import numpy as np

data = np.random.rand(8)           # 8 random floats between 0 and 1
data = data * 100                  # 1. normalize
filtered = data[data > 50]         # 2. values greater than 50
print(np.sort(filtered))           # 3. sorted (ascending)
