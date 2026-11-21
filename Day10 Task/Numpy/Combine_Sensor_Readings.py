# Combine Two Sensor Readings
""" Sensor1 = [10, 20, 30]   Sensor2 = [40, 50, 60]
 Task: Store in arrays and combine using concatenation."""

import numpy as np

#Store each sensor's readings in its own array.
sensor1 = np.array([10, 20, 30])
sensor2 = np.array([40, 50, 60])
#np.concatenate() joins arrays end to end (takes a tuple/list of arrays).
combined = np.concatenate((sensor1, sensor2))
print("Combined readings:", combined)   # [10 20 30 40 50 60]
