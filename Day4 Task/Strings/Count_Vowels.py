#Write a program to count the number of vowels in a string.  

main_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in main_string:
    if char in vowels:
        count+=1
print("number of vowels:", count)
    


