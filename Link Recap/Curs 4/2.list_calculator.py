numbers=[]

while True:
    user=input("Please add numeric values:\n")
    if user.isnumeric():
        user=int(user)
        numbers.append(user)

    elif not user:
        print("the sum is:", sum(numbers))
        numbers=[]
    elif user=="Exit":
        break

    else:
        print("Non numeric value!!")
