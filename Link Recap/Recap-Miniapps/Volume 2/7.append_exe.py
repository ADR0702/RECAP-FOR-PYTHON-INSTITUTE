list_name=[]
while True:
    user=input("Please add a name:\n")
    if user=="stop":
        print("Thank you! have a great day!")
        break
    else:
        list_name.append(user)
        print(f"The list is {list_name}")
        