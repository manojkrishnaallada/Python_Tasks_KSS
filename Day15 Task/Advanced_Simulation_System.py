#Advanced Simulation System 
"""Scenario: 
Simulate exam results and generate reports. 
Task: 
● Generate random marks using random 
● Store in NumPy array 
● Convert to Pandas DataFrame 
● Use OOP to represent Student 
● Use conditions + loops to assign grades 
● Save report to file 
● Handle errors using try-except 
● Use math module for statistics"""

import random
import math
import numpy as np
import pandas as pd
 
 
# class to represent student
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = ""
 
    def set_grade(self):
        if self.marks >= 90:
            self.grade = "A"
        elif self.marks >= 70:
            self.grade = "B"
        elif self.marks >= 50:
            self.grade = "C"
        else:
            self.grade = "Fail"
 
 
try:
    # generate random marks
    marks_list = []
    for i in range(5):
        marks_list.append(random.randint(30, 100))
 
    # store in numpy array
    marks_array = np.array(marks_list)
 
    # create student objects and assign grades
    names = []
    grades = []
    for i in range(5):
        s = Student("Student" + str(i + 1), marks_array[i])
        s.set_grade()
        names.append(s.name)
        grades.append(s.grade)
 
    # convert to dataframe
    df = pd.DataFrame({"Name": names, "Marks": marks_array, "Grade": grades})
    print(df)
 
    # statistics using math module
    average = math.fsum(marks_list) / len(marks_list)
    print("Average:", average)
    print("Square root of average:", math.sqrt(average))
 
    # save report to file
    file = open("report.txt", "w")
    file.write(df.to_string())
    file.write("\nAverage: " + str(average))
    file.close()
 
except:
    print("Something went wrong")
