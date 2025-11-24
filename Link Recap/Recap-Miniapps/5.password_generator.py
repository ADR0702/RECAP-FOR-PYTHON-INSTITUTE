# 3. Simple password generator
# Requierments:
# Ask the User the lenght of the password and generate a password using numbers and characters
# You don't need external libraries — only string and random (they are built-in).
# Hints:
# you're going to use for, functions and data types
import random
import string


def pass_generator():
    user=int(input("Please select how many digits your password you want to have:\n"))
    password=""
    for i in range(user):
        password+=random.choice(string.ascii_letters+string.digits)

    print(f"The Password generated for you is{password}")
    return password


pass_generator()