# 3. Employee Data Copy Issue (Shallow vs Deep Copy)
# A company stores employee data:
# employees = [[101, "A"], [102, "B"], [103, "C"]]
# Scenario:
# ● Create a shallow copy of the list.
# ● Modify one nested list (e.g., change "A" to "Z").
# ● Observe changes in both lists.
# Task:
# ● Explain why the change reflects in both.
# ● Fix it using deep copy.

# Solution
import copy

# ---- Shallow copy ----
employees = [[101, "A"], [102, "B"], [103, "C"]]
shallow = copy.copy(employees)     # copies only outer list, inner lists are shared
shallow[0][1] = "Z"                # change "A" to "Z"
print(employees)                   # [[101, 'Z'], ...] -> original also changed
print(shallow)                     # [[101, 'Z'], ...]

# ---- Fix using deep copy ----
employees = [[101, "A"], [102, "B"], [103, "C"]]
deep = copy.deepcopy(employees)    # copies outer AND inner lists
deep[0][1] = "Z"
print(employees)                   # [[101, 'A'], ...] -> original unchanged
print(deep)                        # [[101, 'Z'], ...]
