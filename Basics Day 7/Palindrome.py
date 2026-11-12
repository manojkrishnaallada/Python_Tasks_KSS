#Write a program to check whether a number is a Palindrome.

num = input("Enter a number: ")
pld = num[::-1]
if num == pld:
          print("Its a palindrome")
else:
    print("Not palindrome")
