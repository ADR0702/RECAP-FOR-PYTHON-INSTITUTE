values = [1, 6, 9, 12, 4]

even_five=[]

for nr in values:
    if nr % 2 == 0 and nr > 5:
        even_five.append(nr)

print(f"the numbers that are even and bigger than 5 are: {', '.join(map(str, even_five))}")

