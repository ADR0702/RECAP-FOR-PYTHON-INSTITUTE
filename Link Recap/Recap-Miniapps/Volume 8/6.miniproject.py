name = input("please add a name\n")
age = input("please add your age\n")
password = input("please add a password:\n")

valid = True

if not name.isalpha():
    print("Invalid Name")
    valid = False

if not age.isdigit():
    print("Invalid Age")
    valid = False

if len(password) < 6:
    print("Password too short")
    valid = False

if valid:
    print("FORMULAR VALID")