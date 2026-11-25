# Combine NumPy Arrays into DataFrame 
"""Two arrays: 
names = np.array(["A", "B", "C"]) 
marks = np.array([80, 90, 70]) 
Task: 
● Create a DataFrame with columns "Name" and "Marks" 
● Filter students with marks above 75"""

import numpy as np
import pandas as pd
names = np.array(["A", "B", "C"])
marks = np.array([80, 90, 70])
# A dict maps column name -> array
df8 = pd.DataFrame({"Name": names, "Marks": marks})
# Boolean filtering on the Marks column
print(df8[df8["Marks"] > 75])
 
