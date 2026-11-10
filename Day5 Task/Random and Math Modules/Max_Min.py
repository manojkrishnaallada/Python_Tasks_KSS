#Generate 20 random numbers between 1 and 200 in a list. Using math, display the max, min, sqrt of the max and log of the min.

from math import *
from random import *

numbers = []

for i in range(20):
    ran_list = randint(1, 200)
    numbers.append(ran_list)
print(f"Numbers: {numbers}")

maximum = max(numbers)
minimum = min(numbers)

print(f"Maximum value: {maximum}")
print(f"Minimum value: {minimum}")
print(f"Square root of maximum: {sqrt(maximum)}")
print(f"Logarithm of minimum: {log(minimum)}")
