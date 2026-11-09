#sort the marks in descending order and print the top two students.

students = {"Rahul": 85, "Amit": 92, "Priya": 78, "Sneha": 95}
sorted_students = sorted(students, key=students.get, reverse=True)
for name in sorted_students[:2]:
    print(name, students[name])
