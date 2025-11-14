
numbers=[]

for i in range(6):
    user=input("Please add numeric values:\n")
    while not user.isnumeric():
        print("Non numeric value!!")
        user=input("Please add numeric values:\n")
        
    user=int(user)
    numbers.append(user)


print("list a is:", numbers[:3])
print("list b is:", numbers[3:])

# version 2

no_list=[]
for j in range(2):
    numbers=[]
    for i in range(3):
        numbers.append(i)
    no_list.append(numbers)
print(no_list)

