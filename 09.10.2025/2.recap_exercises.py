user=input("Please write something\n")
print(type(user))

print(str(user))
print(type(user))

print(bool(user))
print(type(user))
try:
    print(int(user))
    print(type(user))

    print(float(user))
    print(type(user))
except ValueError:
    print("you didn't add a number")
    