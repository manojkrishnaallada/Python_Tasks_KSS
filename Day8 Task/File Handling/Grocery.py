# A user wants to save grocery items in a file grocery.txt. Write a Python program that takes multiple items from the user and writes them into the file, with each item on a new line.
 
# Ask how many items the user wants to enter
n = int(input("How many items? "))
 
# "w" = write mode: creates the file (or replaces old content)
with open("grocery.txt", "w") as f:
    for i in range(n):                 # repeat n times
        item = input("Enter item: ")
        f.write(item + "\n")           # each item on a new line
