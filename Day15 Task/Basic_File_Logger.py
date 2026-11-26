#Basic File Logger 
"""Scenario: 
A system logs user actions. 
Task: 
● Take user input 
● Store logs in a file 
● Use loop to allow multiple entries 
● Handle file errors using exception handling"""

try:
    file = open("log.txt", "a")      # "a" adds new lines at the end
 
    while True:                      # loop for multiple entries
        action = input("Enter action (type exit to stop): ")
        if action == "exit":
            break
        file.write(action + "\n")
 
    file.close()
    print("Logs saved")
 
except:
    print("File error")

