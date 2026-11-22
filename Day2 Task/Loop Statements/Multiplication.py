#Write a program to print the multiplication table of a number using a loop.

number = int(input("Enter a number: "))
for x in range(1,11):
    print(f"{number}x{x}={number*x}")
