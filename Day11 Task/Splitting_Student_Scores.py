# 14. Splitting Student Scores Across Servers
# A dataset:
# [50, 60, 70, 80, 90, 100, 110, 120]
# Scenario:
# A distributed system needs to divide this data among 4 servers.
# Task:
# ● Convert to NumPy array.
# ● Split the array into 4 equal parts using array_split().

# Solution
import numpy as np

scores = np.array([50, 60, 70, 80, 90, 100, 110, 120])
parts = np.array_split(scores, 4)      # 8 elements / 4 servers = 2 each
print(parts)
