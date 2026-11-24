#Missing City Data (NaN Handling) 
"""A dataset contains city populations: 
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000} 
Scenario: 
You want data for: 
["Delhi", "Chennai", "Bangalore"] 
Task: 
● Create a Series with the above index 
● Identify which cities have missing values (NaN)"""

import pandas as pd
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}
s = pd.Series(cities, index=["Delhi", "Chennai", "Bangalore"])
print("SEries:\n", s)
print("Missing values:\n", s.isnull())
print("City with NaN:", s[s.isnull()].index[0])
