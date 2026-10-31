#Write a program that searches for a number in a list and breaks the loop when found.

numbers = [10, 20, 30]
search = int(input("Enter a number: "))
for i in numbers:
    if i == search:
        print("Number found")
        break
else:
    print("Number not found")
