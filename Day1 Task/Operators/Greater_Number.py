#Write a program to check if one number is greater than another.
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
if x>y:
    print(x, "is greater than", y)
elif y>x:
    print(y, "is greater than", x)
          
else:
    print("invalid")
