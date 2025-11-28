user=input("please type something, everything:\n")
print(type(user))
if user.isdigit():
    print(int(user))
else:
    print("user cannot be an integer")

