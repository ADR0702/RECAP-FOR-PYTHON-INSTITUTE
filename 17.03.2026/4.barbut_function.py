import random

def roll_the_dice(player_name):
    dice1=random.randint(1, 6)
    dice2=random.randint(1, 6)
    total=dice1+dice2
    print(f"the player {player_name} rolled {dice1} and {dice2}")
    return total

while True:
    total1=roll_the_dice("User 1")
    total2=roll_the_dice("User 2")
    if total1 > total2:
        print("User 1 won!!")
        break
    elif total2 > total1:
        print("User 2 won!")
        break
    else:
        print("Draw!")
    continue
