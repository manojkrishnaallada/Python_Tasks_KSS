#Write a Python program using the math module to calculate and display the square root, floor value, and ceiling value of a number entered by the user.

from math import *
num = float(input("Enter a number: "))
print(f"Square root: {sqrt(num)}")
print(f"Floor value: {floor(num)}")
print(f"Ceiling value: {ceil(num)}")
