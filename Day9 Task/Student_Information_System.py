"""
A school wants a program to store student details. Create a Student class with 
attributes such as name, roll number, and marks. Create objects for at least three 
students and display their details. """


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

s1 = Student("Asha", 1, 88)
s2 = Student("Ravi", 2, 75)
s3 = Student("Meena", 3, 92)
for s in (s1, s2, s3):
    s.display()
