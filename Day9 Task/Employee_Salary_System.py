"""
A company has two types of employees: Employee and Manager. Create a base class 
Employee containing name and salary. Create a derived class Manager that inherits 
from Employee and displays the employee details."""

class Employee3:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee3):
    pass  # inherits everything from Employee3

Manager("Kiran", 90000).display()
