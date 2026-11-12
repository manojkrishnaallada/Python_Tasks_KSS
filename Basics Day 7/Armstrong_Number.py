#Write a program to check whether a given number is an Armstrong number or not.

num = int(input("Enter a number: "))
num_str = str(num)
power = len(num_str)
total_sum = 0
for digit in num_str:
          total_sum += int(digit) ** power
print(total_sum)
if total_sum == num:
          print("Its an armstrong number")
else:
    print("Not an armstrong number")
    
