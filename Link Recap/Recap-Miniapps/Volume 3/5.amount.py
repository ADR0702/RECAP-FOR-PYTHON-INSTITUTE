numbers=[]
while True:
    user=input("Please add a number and when you want to total amount type stop\n")
    if user.isdigit():
        user=int(user)
        numbers.append(user)
    elif user=="stop":
        print(f"the sum of { numbers}  are {sum(numbers)}")
        break
    else:
        print("Please add a number or stop")