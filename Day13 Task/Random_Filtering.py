#Random Data & Filtering 
"""Generate random numbers: 
nums = np.random.randint(1, 100, 10) 
Task: 
● Filter values that are divisible by 5 
● Return sorted result."""

import numpy as np
nums = np.random.randint(1, 100, 10)
print("Random numbers:", nums)
result = nums[nums % 5 == 0]
print("Sorted numbers divisible by 5:", np.sort(result))
