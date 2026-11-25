# Basic DataFrame Creation from NumPy 
"""You have: 
data = np.array([[1, 2], [3, 4], [5, 6]]) 
Task: 
● Convert it into a Pandas DataFrame 
● Add column names: "X", "Y"""

import numpy as np
import pandas as pd
data = np.array([[1, 2], [3, 4], [5, 6]])
# Each inner row becomes a DataFrame row; `columns` names the columns
df2 = pd.DataFrame(data, columns=["X", "Y"])
print(df2, "\n")
