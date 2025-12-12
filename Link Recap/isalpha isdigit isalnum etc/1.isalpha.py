user=input("Please add a name:\n")
check=True
for i in user:
    if not i.isalpha():
        check=False

if check:
    print("Name Valid")
else:
    print("Invalid name")