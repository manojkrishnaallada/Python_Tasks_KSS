# Smart Data Processing Pipeline 
"""Scenario: 
A system processes numeric data from file. 
Task: 
● Read numbers from a file 
● Use NumPy for calculations (mean, std) 
● Convert results to Pandas DataFrame 
● Use exception handling for bad data 
● Use a generator to stream data 
● Apply decorator to measure execution time"""

import time
import numpy as np
import pandas as pd
 
# create a sample file (abc is bad data)
file = open("numbers.txt", "w")
file.write("10\n20\nabc\n30\n40\n")
file.close()
 
 
# decorator to measure execution time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time taken:", end - start)
    return wrapper
 
 
# generator to stream data one number at a time
def read_numbers():
    file = open("numbers.txt")
    for line in file:
        try:
            yield float(line)
        except ValueError:                   # handle bad data
            print("Bad data skipped:", line.strip())
    file.close()
 
 
@timer
def process():
    numbers = []
    for n in read_numbers():
        numbers.append(n)
 
    # numpy calculations
    mean = np.mean(numbers)
    std = np.std(numbers)
 
    # convert results to dataframe
    df = pd.DataFrame({"Mean": [mean], "Std": [std]})
    print(df)
 
 
process()
