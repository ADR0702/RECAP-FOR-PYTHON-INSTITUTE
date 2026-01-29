text = "Python 3 este cool"
numbers=0
string=0
space=0

for i in text:
    if i.isdigit():
        numbers+=1
    elif i.isalpha():
        string+=1
    elif i.isspace():
        space+=1

print(f"there are {string} string characters, {numbers} numbers and {space} spaces")