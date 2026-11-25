#Find Maximum Value 
"""A dataset: 
arr = np.array([12, 45, 22, 67, 34]) 
Task: 
● Convert to Pandas Series 
● Find the maximum value"""

import numpy as np
import pandas as pd
arr = np.array([12, 45, 22, 67, 34])
s4 = pd.Series(arr)
# .max() is the Pandas method (np.max(s4) works too)
print("Max =", s4.max(), "\n")
