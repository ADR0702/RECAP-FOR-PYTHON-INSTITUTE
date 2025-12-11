count=0
while True:
    user=input("Please add a number:\n")
    if user.isdigit():
        user=int(user)
        count+=user
    elif user=="stop":
        print(f"total amount is {count}")
        break
    else:
        print("The character you added is not a number")