#Write a function to check whether a number is even or odd. 

def check_even_odd(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
n = int(input("Enter a number: "))
print(f"The number is {check_even_odd(n)}")
