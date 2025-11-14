
suma=0
while True:
    user=input("Please add numeric values:\n")
    if user.isnumeric():
        user=int(user)
        suma= suma+user

    elif not user:
        print("the sum is:", suma)
        suma=0

    else:
        print("Non numeric value!!")
