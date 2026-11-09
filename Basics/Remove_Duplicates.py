#Remove duplicates from [1, 2, 3, 2, 4, 1, 5, 3] keeping original order.

numbers = [1, 2, 3, 2, 4, 1, 5, 3]
empty = []
for num in numbers:
    if num not in empty:
        empty.append(num)
print(empty)
