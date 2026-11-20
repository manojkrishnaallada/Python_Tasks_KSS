"""Create a generator function that continuously generates even numbers starting from 
2. The program should print the first N even numbers using this generator. """

def even_numbers():
    n = 2
    while True:                                     # endless loop
        yield n                                     # give n and pause
        n = n + 2                                   # next even number

N = 5
count = 0
for num in even_numbers():
    print(num)
    count = count + 1
    if count == N:                                  # got N numbers, so stop
        break
