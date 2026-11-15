# A student stores daily notes in a file called notes.txt. Write a program that opens the file, reads all the contents, and displays them on the screen.
 
# Open the file in read mode
with open("notes.txt", "r") as f:
    print(f.read())   # read everything and print it
