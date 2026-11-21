# A company stores employee data in a file employees.txt in the format: EmployeeName Salary (Example: Ramesh 25000). Write a Python program that reads employee data from the file, displays all employee details, finds the employee with the highest salary, and appends a new employee record to the file.
 
highest_name = ""    # name of the top earner
highest_salary = 0   # highest salary found so far
 
with open("employees.txt", "r") as f:
    for line in f:
        parts = line.split()                 # "Ramesh 25000" -> ["Ramesh", "25000"]
        if len(parts) == 2:
            print(parts[0], parts[1])        # display employee details
            if int(parts[1]) > highest_salary:   # compare with highest so far
                highest_salary = int(parts[1])
                highest_name = parts[0]
 
print("Highest Salary:", highest_name, highest_salary)
 
# Take new employee details from the user
name = input("Enter new employee name: ")
salary = input("Enter salary: ")
 
# Append the new record at the end of the file
with open("employees.txt", "a") as f:
    f.write("\n" + name + " " + salary)
