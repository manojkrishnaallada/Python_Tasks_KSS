# 5. Nested Data Independence (Deep Copy)
# A school stores classroom data:
# classes = [["Math", [30, 35]], ["Science", [25, 28]]]
# Scenario:
# ● Create a deep copy of this structure.
# ● Modify student count in original.
# Task:
# ● Prove that copied data remains unchanged.
# ● Explain why deep copy is required here.

# Solution
import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]
copied = copy.deepcopy(classes)    # independent copy of every nested level

classes[0][1][0] = 100             # modify student count in original
print(classes)                     # [['Math', [100, 35]], ['Science', [25, 28]]]
print(copied)                      # [['Math', [30, 35]], ['Science', [25, 28]]] -> unchanged
