user=input("Please add a positive or a negative number:\n")
user=int(user)

if user < 0:
    print("the number is negative")
elif user ==0:
    print("the number is zero")
else:
    print("the number is positive")