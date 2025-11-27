# What you need to do:
# Using a list, allow the user to:
# add a name
# delete a name
# see the complete list
# exit the program
# You should have a menu that repeats (while True).

name_list=[]
while True:
    user_options=input("Choose action: Add name, delete name, see list, exit\n").lower()
    if user_options=="add name":
        user_name=input("Please type the name:\n")
        name_list.append(user_name)
    elif user_options=="delete name":
        user_name=input("Please type the name you want to delete:\n")
        name_list.remove(user_name)
    elif user_options=="see list":
        print(f"the people on the list are:{name_list}")
    elif user_options=="exit":
        print("Thank you! Have a great day!")
        break
    else:
        user_options=input("The choosen option doesn't exist! Please choose action: Add name, delete name, see list, exit\n").lower()
    