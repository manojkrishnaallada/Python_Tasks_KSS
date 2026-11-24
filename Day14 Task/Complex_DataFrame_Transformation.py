#Complex DataFrame Transformation 
"""A DataFrame: 
df = pd.DataFrame({ 
"Name": ["A", "B", "C", "D"], 
"Marks": [50, 80, 30, 90] 
}) 
Scenario: 
● Students scoring below 50 failed 
Task: 
1. Create a column Status ("Pass"/"Fail") 
2. Filter only passed students 
3. Calculate average marks of passed students"""

import pandas as pd
df = pd.DataFrame({"Name": ["A", "B", "C", "D"], "Marks": [50, 80, 30, 90]})
df["Status"] = "Fail"
df.loc[df["Marks"] >= 50, "Status"] = "Pass"
print("status:\n", df)
passed = df[df["Status"] == "Pass"]
print("Passed students:\n", passed)
print("Avg marks of passed students:", passed["Marks"].mean())
