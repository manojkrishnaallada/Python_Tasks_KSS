#Write a program that uses random.choice() to randomly select a student from a list and display: "The selected student for presentation is: <name>".

from random import *
students = ["Manoj", "Krishna", "Charan", "Vijay", "Rashmika", "Anushka", "Kajal"]
selected = choice(students)
print(f"The selected student for presentation is : {selected}")
