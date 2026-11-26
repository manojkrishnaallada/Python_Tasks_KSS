# Random Number Analyzer 
"""Scenario: 
A system generates random numbers for testing. 
Task: 
● Use random to generate 10 numbers 
● Store in a list 
● Use loop + condition to count even/odd numbers 
● Use set to remove duplicates"""

import random
 
numbers = []
 
# generate 10 random numbers and store in list
for i in range(10):
    numbers.append(random.randint(1, 20))
print("Numbers:", numbers)
 
# count even and odd
even = 0
odd = 0
for n in numbers:
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even:", even)
print("Odd:", odd)
 
# set removes duplicates
print("Without duplicates:", set(numbers))
