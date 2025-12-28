numbers = [4, -2, 7, 0, -5, 10]

positive_no=[]
negative_no=[]
zero="Fuck you!"
for nr in numbers:
    if nr > 0:
        positive_no.append(nr)
    elif nr < 0:
        negative_no.append(nr)
    else:
        zero

print(f"the positive numbers are : {', '.join(map(str, positive_no))} , the negative numbers are {', '.join(map(str, negative_no))} and zero is {zero}")
