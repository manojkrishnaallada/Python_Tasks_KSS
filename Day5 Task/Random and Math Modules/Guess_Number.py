#Create a number guessing game that program generates a random number from 1 to 50. User has 5 attempts. After each guess, use math.fabs() to show how far the guess is from the correct number.

from math import *
from random import *

secret = randint(1, 50)
attempts = 5
print("Guess the number between 1 and 50: ")
print("You only have 5 attempts: ")

for i in range(1, attempts + 1):
    guess = int(input(f"Attempt-{i}:\nEnter your guess number: "))
    difference = fabs(guess - secret)

    if guess == secret:
        print(f"You guessed it in {i} attempts.")
        break
    else:
        print(f"Wrong! Your guess is {int(difference)} from the correct number.")
if guess != secret:
    print(f"Game over! The correct number was {secret}")
