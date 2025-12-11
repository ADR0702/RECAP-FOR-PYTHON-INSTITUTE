# What you need to do:
# The program chooses a number between 1 and 20.
# The user guesses until they find it.
# We use:
# while
# conditions
# break when guess

import random

pc_number = random.randint(1, 20)

user = int(input("Please choose a number from 1 to 20:\n"))

while user != pc_number:
    print("Wrong! Guess again")
    user = int(input("Please choose a number from 1 to 20:\n"))

print("Correct answer!")
