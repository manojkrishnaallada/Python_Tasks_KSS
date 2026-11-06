#Write a program to check whether a string is a palindrome.

s = input("Enter a string: ")
s.lower()
p = s[::-1]
if s == p:
    print("palindrome")
else:
    print("not palindrome")
    


