#Write a program to assign grades based on marks (for example: A, B, C, Fail). 

marks = int(input("Enter your marks: "))
if marks<0 and marks>100:
    print("invalid marks")
elif marks>=90:
    print("grade A")
elif marks>=75:
    print("grade B")
elif marks>=40:
    print("grade C")
else:
    print("fail")
