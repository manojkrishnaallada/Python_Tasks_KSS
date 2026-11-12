#Write a program to check whether a given number is a Strong number.

num = int(input("Enter a number: "))
temp = num
sum_of_factorials = 0
for digit_char in str(num):
    digit = int(digit_char)
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum_of_factorials += fact
if sum_of_factorials == num:
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")
    
