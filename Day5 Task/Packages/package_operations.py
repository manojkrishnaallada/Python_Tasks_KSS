from utilities import math_operations as m, string_operations as s
num1 = int(input("Enter first number: "))
num2 = int(input("Enter decong number: "))
print(f"'{num1} + {num2}' = {m.add(num1, num2)}")
print(f"'{num1} * {num2}' = {m.multiply(num1, num2)}")

txt = input("Enter a word: ")
print(f"Uppercase: {s.upper_case(txt)}")
print(f"Count: {s.count_characters(txt)}")
