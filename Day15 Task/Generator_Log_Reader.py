# Generator-based Log Reader 
"""Scenario: 
A large log file needs to be processed. 
Task: 
● Create a generator to read file line by line 
● Use loop to process logs 
● Use condition to filter errors 
● Count occurrences using a dictionary"""

# create a sample log file
file = open("server.log", "w")
file.write("INFO started\nERROR disk full\nINFO running\nERROR timeout\nERROR disk full\n")
file.close()
 
 
# generator reads file line by line using yield
def read_logs(filename):
    file = open(filename)
    for line in file:
        yield line.strip()
    file.close()
 
 
count = {}   # dictionary to count errors
 
for line in read_logs("server.log"):
    if "ERROR" in line:                      # filter only errors
        if line in count:
            count[line] = count[line] + 1
        else:
            count[line] = 1
 
print(count)
