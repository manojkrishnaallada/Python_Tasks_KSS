#Create a dictionary of student marks. Add a student, update marks, print all details.

students = {"Manoj": 80, "Charan": 70, "Likith": 60}
students["Lavanth"] = 50 #add new student with marks
students["Likith"] = 40 #update likith marks
for name, marks in students.items():
    print(f"{name} : {marks}")
