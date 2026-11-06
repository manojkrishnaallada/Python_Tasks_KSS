#Write a function to find the sum of elements in a list using a user-defined function. 

def calculate_list_sum(lst):
    total = 0
    for item in lst:
        total += item
    return total
numbers = [1, 2, 3, 4]
print("Sum of elements:", calculate_list_sum(numbers))
