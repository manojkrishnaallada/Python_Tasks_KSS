#find highest salary, filter salary>35,000, calculate average salary, list names.


employees = [
    {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]
#Find the Employee with the Highest Salary

highest_salary_employee = max(employees, key=lambda x: x["salary"])
print(f"highest salary: {highest_salary_employee}")

#Filter Employees Whose Salary is Greater than 35,000

filtered_employees = [e for e in employees if e["salary"] > 35000]
print(f"Salary greater than 35,000 : {filtered_employees}")

#Calculate the Average Salary

average_salary = sum(e["salary"] for e in employees) / len(employees)
print(f"Average salary : {average_salary}")

#Create a List Containing Only Employee Names

employee_names = [e["name"] for e in employees]
print(f"List of employee names : {employee_names}")
