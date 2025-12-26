values = [2, 4, 2, 5, 4, 6]
no_doubles=[]


for nr in values:
    if nr not in no_doubles:
        no_doubles.append(nr)

print(f"The numbers that don't repeat are {', '.join(map(str, no_doubles))}")