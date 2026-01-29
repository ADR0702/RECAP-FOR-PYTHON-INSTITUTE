user=input("Please add a number:\n")

while not user.isdigit():
    user=input("you didnt add a number!! Please add a number:\n")
    
user=int(user)
if user > 0:
    print(f"the number {user} is positive")
elif user == 0:
    print(f"the number {user} is zero")
else:
    print(f"the number {user} is negative")

  