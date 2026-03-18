import random

while True:
    

    zar1=random.randint(1, 6)
    zar2=random.randint(1, 6)
    total1=zar1+zar2
    print(f"User 1 spinned {zar1} for dice 1 and {zar2} for dice 2")



    zar3=random.randint(1, 6)
    zar4=random.randint(1, 6)
    total2=zar3+zar4
    print(f"User 2 spinned {zar3} for dice 1 and {zar4} for dice 2")
    if total1 > total2:
        print("User 1 won!")
        break
    elif total1 < total2:
        print("User 2 won!")
        break
    else:
        print("Draw!")
        continue
