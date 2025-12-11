import random

def number_check(value):
    while True:
        value=input("Please add a number between 1 and 20: \n")
        if not value.isnumeric():
            print("that's not a number, try again!")
            continue
        value=int(value)
        if value < 1 or value >20:
            print("The number must be between 1 and 20!")
            continue
        return value
    

pc_numbers=random.randint(1, 20)
user=number_check()

while user != pc_numbers:
    print("Wrong Number Guess Again:\n")
    user=number_check()

print("FINALLY! I GUESSED YOUR FUCKING NUMBER!")
