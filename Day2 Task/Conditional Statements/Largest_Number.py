#Write a program to find the largest of three numbers using if-elif-else. 

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a>=b and a>=c:
    print(f"{a} is largest")
elif b>=a and b>=c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")

    
