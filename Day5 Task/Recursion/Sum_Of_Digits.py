#Write a recursive function to calculate the sum of digits of a number. 

def sum_of_digits(n):
    n = abs(n)
    if n<10:
        return n
    return (n%10) + sum_of_digits(n//10)
print(sum_of_digits(123))
