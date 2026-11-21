# Inventory Update System
""" Inventory = [[10, 15], [20, 25]]
  Task: Add 2 to every element and print the updated inventory."""

import numpy as np
#Create the inventory matrix.
inventory = np.array([[10, 15], [20, 25]])
#Adding 2 applies to every element in the matrix.
inventory = inventory + 2
print("Updated inventory:\n", inventory)   # [[12 17] [22 27]]
 
