numbers=[]

contor=0
while contor < 6:
    user=input("Please add numeric values:\n")
    if user.isnumeric():
        user=int(user)
        numbers.append(user)
        contor+=1
    else:
        print("Non numeric value!!")
print("suma este:", sum(numbers))


# version2
numbers=[]

while len(numbers) < 6:
    user=input("Please add numeric values:\n")
    if user.isnumeric():
        user=int(user)
        numbers.append(user)
    else:
        print("Non numeric value!!")
print("suma este:", sum(numbers))

# version 3

numbers=[]

for i in range(6):
    user=input("Please add numeric values:\n")
    while not user.isnumeric():
        print("Non numeric value!!")
        user=input("Please add numeric values:\n")
        
    user=int(user)
    numbers.append(user)
    
print("suma este:", sum(numbers))