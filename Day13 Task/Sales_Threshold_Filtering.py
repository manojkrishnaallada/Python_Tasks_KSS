#Sales Threshold Filtering 
"""You are given monthly sales: 
sales = np.array([12000, 18000, 9000, 22000, 15000, 30000]) 
Task: 
● Filter all sales values greater than the average sales 
● Return the filtered array."""

import numpy as np
sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])
avg = np.mean(sales)
result = sales[sales > avg]
print("Average:", avg)
print("Filtered sales:", result)
