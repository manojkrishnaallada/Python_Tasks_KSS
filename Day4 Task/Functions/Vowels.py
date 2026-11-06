#Write a function that takes a string as input and returns the number of vowels. 

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
string_input = input("Enter a string: ")
print("Number of vowels:", count_vowels(string_input))
