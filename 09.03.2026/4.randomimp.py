import random

ana_maria_stan=int(input("Beautiful and sweet Ana Maria, please choose a number between 1 and 10:\n"))
random_number=random.randint(1,10)

if ana_maria_stan == random_number:
    print("congragiulations darling! you guessed the number!")
else:
    print(f"You suck! the number choosed by the computer is {random_number} ! Please try again!")





