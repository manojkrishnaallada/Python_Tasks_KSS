# Row Filtering + Aggregation 
"""A dataset: 
arr = np.array([ 
[100, 200], 
[150, 250], 
[80, 120], 
[300, 400] 
]) 
Task: 
● Convert to DataFrame with columns "Sales", "Profit" 
● Filter rows where Sales > 100 
● Find average Profit of filtered rows"""

import numpy as np
import pandas as pd
arr = np.array([
    [100, 200],
    [150, 250],
    [80, 120],
    [300, 400]
])
df10 = pd.DataFrame(arr, columns=["Sales", "Profit"])
# Keep rows where Sales > 100 (strictly greater, so the 100 row is excluded)
filtered = df10[df10["Sales"] > 100]
# Average Profit of remaining rows: (250 + 400) / 2 = 325
print(filtered)
print("Average Profit:", filtered["Profit"].mean())
