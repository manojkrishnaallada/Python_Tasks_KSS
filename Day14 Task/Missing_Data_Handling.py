#Missing Data Handling (NumPy + Pandas) 
"""A dataset: 
arr = np.array([10, np.nan, 30, np.nan, 50]) 
Task: 
● Convert to Pandas Series 
● Replace NaN values with the mean of the Series 
● Print updated data"""

import numpy as np
import pandas as pd
arr = np.array([10, np.nan, 30, np.nan, 50])
s9 = pd.Series(arr)
# .mean() skips NaN by default: (10 + 30 + 50) / 3 = 30
# fillna() replaces every NaN with that mean
s9 = s9.fillna(s9.mean())
print(s9)
