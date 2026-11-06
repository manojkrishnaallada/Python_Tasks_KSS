#Write a function that returns the factorial of a number. 
def calc_factorial(n):
    if n < 0:
        return "Invalid"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input("Enter a positive integer: "))
print("Factorial:", calc_factorial(num))
