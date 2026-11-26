# Data Analysis Tool (NumPy + Pandas) 
"""Scenario: 
Analyze student marks. 
Task: 
● Generate marks using NumPy 
● Convert into Pandas DataFrame 
● Use conditions to filter passing students 
● Calculate mean using math/NumPy 
● Use loop to print results""" 

import numpy as np
import pandas as pd
 
# generate 6 random marks using numpy
marks = np.random.randint(20, 100, 6)
 
# convert to dataframe
df = pd.DataFrame({"Marks": marks})
print(df)
 
# filter passing students (marks >= 40)
passed = df[df["Marks"] >= 40]
print("Passed students:")
print(passed)
 
# mean using numpy
print("Mean:", np.mean(marks))
 
# loop to print results
for m in marks:
    if m >= 40:
        print(m, "Pass")
    else:
        print(m, "Fail")

