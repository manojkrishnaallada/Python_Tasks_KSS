#Write a Python program with a function that returns the largest of three numbers.

def find_max_of_three(a, b, c):
    if a >= b and a >=c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
print("The largest number is:", find_max_of_three(n1, n2, n3))
