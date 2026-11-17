"""A university has different staff types such as Professor, LabAssistant, and 
Administrator. All inherit from a base class Staff. Implement hierarchical inheritance 
to manage and display their information. """

class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name} - Salary: {self.salary}", end=" | ")

class Professor(Staff):
    def __init__(self, name, salary, subject):
        super().__init__(name, salary)
        self.subject = subject
    def display(self):
        super().display()
        print("Subject:", self.subject)

class LabAssistant(Staff):
    def __init__(self, name, salary, lab):
        super().__init__(name, salary)
        self.lab = lab
    def display(self):
        super().display()
        print("Lab:", self.lab)

class Administrator(Staff):
    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.dept = dept
    def display(self):
        super().display()
        print("Department:", self.dept)

for person in [Professor("Dr. Rao", 100000, "Maths"),
               LabAssistant("Sita", 30000, "Physics Lab"),
               Administrator("Mohan", 50000, "Admissions")]:
    person.display()
