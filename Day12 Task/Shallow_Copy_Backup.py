# 1. Student List Backup (Shallow Copy)
# A teacher has a list of student marks:
# marks = [50, 60, 70, 80]
# Scenario:
# She creates a backup using assignment:
# backup = marks
# Task:
# ● Modify the first element in marks.
# ● Observe the change in backup.
# ● Explain why both lists are affected.

# Solution
marks = [50, 60, 70, 80]
backup = marks         # no new list, just a second name for the same list

marks[0] = 99          # modify first element in marks
print(marks)           # [99, 60, 70, 80]
print(backup)          # [99, 60, 70, 80] -> backup changed too
print(marks is backup) # True -> both names point to the same list in memory
