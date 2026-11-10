#Write a python program that imports calculator.py ad perform calculations based on user input.

from calculator import *

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Addition: {add(num1, num2)}")
print(f"Subtraction: {subtract(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division: {divide(num1, num2)}")
