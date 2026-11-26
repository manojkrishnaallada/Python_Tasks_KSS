#Employee Management System (OOP + File + Dict) 
"""Scenario: 
Manage employee data. 
Task: 
● Create a class Employee 
● Store employees in a dictionary 
● Save data to a file 
● Use exception handling for invalid salary input 
● Use loop to display all employees"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
 
    def show(self):
        print("Name:", self.name, "Salary:", self.salary)
 
 
# dictionary to store employees
employees = {}
 
for i in range(3):
    emp_id = input("Enter employee id: ")
    name = input("Enter name: ")
    try:
        salary = int(input("Enter salary: "))
        employees[emp_id] = Employee(name, salary)
    except ValueError:
        print("Invalid salary! Employee not added.")
 
# save data to file
file = open("employees.txt", "w")
for emp_id in employees:
    emp = employees[emp_id]
    file.write(emp_id + "," + emp.name + "," + str(emp.salary) + "\n")
file.close()
 
# display all employees using loop
for emp_id in employees:
    print("ID:", emp_id)
    employees[emp_id].show()
    
