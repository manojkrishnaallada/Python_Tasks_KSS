# A teacher wants to store student attendance in a file named attendance.txt. Write a Python program that takes a student name as input and appends it to the file. Then display the contents of the file.
 
# Take student name from the user
name = input("Enter student name: ")
 
# "a" = append mode: adds new data at the end without deleting old data
with open("attendance.txt", "a") as f:
    f.write(name + "\n")   # \n moves to the next line
 
# "r" = read mode: open the file to display its contents
with open("attendance.txt", "r") as f:
    print(f.read())        # read() gives the whole file as one string
