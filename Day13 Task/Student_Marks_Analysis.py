#Student Marks Analysis 
"""Given marks of 5 students in 3 subjects: 
marks = np.array([ 
[70, 80, 90], 
[60, 75, 85], 
[50, 65, 70], 
[90, 95, 85], 
[40, 55, 60] 
]) 
Task: 
● Calculate total marks of each student. 
● Identify students whose total marks are above the class average."""

import numpy as np
marks = np.array([ 
    [70, 80, 90], 
    [60, 75, 85], 
    [50, 65, 70], 
    [90, 95, 85], 
    [40, 55, 60] 
])
total = np.sum(marks, axis=1) #total of each student
class_avg = np.mean(total)  #class average
print("Total marks:", total)
print("Class average:", class_avg)
print("Students above average (index):", np.where(total > class_avg)[0])
print("Their total marks:", total[total > class_avg])
