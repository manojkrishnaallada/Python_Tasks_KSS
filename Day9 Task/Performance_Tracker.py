"""A software team wants to track how long functions take to execute. Create a decorator 
that measures and prints the execution time of a function. """

import time   # needed to get the current time

def timer(func):
    def wrapper():
        start = time.time()                         # time before
        func()                                      # run the original function
        end = time.time()                           # time after
        print("Time taken:", end - start, "seconds")
    return wrapper

@timer
def big_sum():
    total = 0
    for i in range(1000000):                        # a long loop so the time is visible
        total = total + i
    print("Sum =", total)

big_sum()
