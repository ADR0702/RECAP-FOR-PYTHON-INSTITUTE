users = {
    "admin": "1234",
    "john": "pass",
    "ana": "qwerty"
}
print('Wellcome sir! For your identification:')
while True:
    pc_user=input("Please add your login username\n")
    if pc_user not in users:
        print("Wrong Username!")
        continue
    password=input("Please add your password:\n")

    if users[pc_user] == password:
        print("Acces Granted!")
        break
    else:
        print("Wrong password!")
