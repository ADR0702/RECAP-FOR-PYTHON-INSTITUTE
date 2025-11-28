my_list = ["a", "b", "c"]
my_string = "xyz"
my_set = {1, 2, 3}
combined= set(my_list) | set(my_string)| my_set
user_input=input("Please add a number or a character:\n")

for i in user_input:
    if i.isdigit():
        value=int(i)
    else:
        value=i
    if i in combined:
        print("Character found")
    else:
        print("Character not found!")