# A teacher stores student marks in a file marks.txt in the format: Name Marks (Example: Rahul 80). Write a Python program to read the file, display all student records, and calculate and display the average marks of the class.
 
total = 0   # sum of all marks
count = 0   # number of students
 
with open("marks.txt", "r") as f:
    for line in f:                     # read file line by line
        parts = line.split()           # "Rahul 80" -> ["Rahul", "80"]
        if len(parts) == 2:            # ignore empty lines
            print(parts[0], parts[1])  # display the record
            total += int(parts[1])     # convert marks to number and add
            count += 1
 
# Average = total marks / number of students
print("Average Marks:", total / count)
