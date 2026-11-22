# 12. Sorting Customer Names
# A system stores customer names:
# ["Ravi", "Anil", "Sita", "John"]
# Task:
# ● Convert it to a NumPy array.
# ● Sort the names alphabetically.

# Solution
import numpy as np

names = np.array(["Ravi", "Anil", "Sita", "John"])
print(np.sort(names))      # alphabetical order -> ['Anil' 'John' 'Ravi' 'Sita']
