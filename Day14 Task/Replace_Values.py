#Replace Values Using NumPy + Pandas 
"""A Series: 
S = pd.Series([10, 50, 30, 80, 20]) 
Task: 
● Replace values greater than 40 with 0 using NumPy logic 
● Return updated Series"""

import numpy as np
import pandas as pd
S7 = pd.Series([10, 50, 30, 80, 20])
# np.where(condition, value_if_true, value_if_false) returns a NumPy array,
# so wrap it back into a Series (keeping the original index)
S7 = pd.Series(np.where(S7 > 40, 0, S7), index=S7.index)
print(S7)
 
