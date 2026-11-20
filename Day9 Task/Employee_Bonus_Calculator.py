"""A company wants to apply a bonus calculation automatically before displaying the 
salary. Create an Employee class and use a decorator that modifies the salary by 
adding a bonus before displaying it. """

def add_bonus(func):
    def wrapper(self):                              # self is needed because get_salary is inside a class
        salary = func(self)                         # normal salary
        return salary + salary * 0.10               # add 10% bonus
    return wrapper

class Employee17:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @add_bonus                                      # bonus is added automatically
    def get_salary(self):
        return self.salary

    def display(self):
        print(self.name, "salary with bonus:", self.get_salary())

emp = Employee17("Anita", 50000)
emp.display()
