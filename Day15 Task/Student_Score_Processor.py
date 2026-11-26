# Student Score Processor 
"""Scenario: 
A teacher stores student names and marks in a list of tuples. 
Task: 
● Convert data into a dictionary 
● Use a loop + condition to find students scoring above 50 
● Use math module to calculate average 
● Store results in a text file"""

import math
 
# list of tuples (name, marks)
data = [("Asha", 78), ("Ravi", 45), ("Meena", 90), ("John", 50)]
 
# convert list of tuples to dictionary
students = dict(data)
 
# find students scoring above 50
print("Students above 50:")
for name in students:
    if students[name] > 50:
        print(name, students[name])
 
# average using math module
total = math.fsum(students.values())
average = total / len(students)
print("Average:", average)
 
# store result in text file
file = open("result.txt", "w")
file.write("Average marks: " + str(average))
file.close()

