#Student Marks Analysis (NumPy → Pandas) 
"""Marks data: 
arr = np.array([ 
[80, 90], 
[70, 60], 
[85, 95] 
]) 
Task: 
● Convert into DataFrame with columns "Math", "Science" 
● Add a new column Total 
● Find student with highest total"""

import numpy as np
import pandas as pd
arr = np.array([
    [80, 90],
    [70, 60],
    [85, 95]
])
df6 = pd.DataFrame(arr, columns=["Math", "Science"])
# New column = row-wise sum of the two subject columns
df6["Total"] = df6["Math"] + df6["Science"]
# idxmax() returns the index label of the largest Total
top = df6["Total"].idxmax()
print(df6)
print("Student with highest total: index", top, "->", df6.loc[top].to_dict())
