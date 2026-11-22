# 2. Device Sensor Value (Scalar Array)
# An IoT device records a single sensor reading = 75.
# Task:
# ● Create a 0-D NumPy array with this value.
# ● Print the value and check its number of dimensions.

# Solution
import numpy as np

sensor = np.array(75)        # single value -> 0-D array
print(sensor)                # 75
print(sensor.ndim)           # 0 -> scalar has zero dimensions
