#Create a python module named calculator.py that contains functions to perform: Addition, Subtraction, Multiplication, Division.

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b
