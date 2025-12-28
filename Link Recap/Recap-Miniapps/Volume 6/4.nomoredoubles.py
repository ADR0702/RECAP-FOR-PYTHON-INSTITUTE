values = [2, 4, 2, 5, 4, 6, 5]
unique_values=[]
unique_number=0

for nr in values:
    if nr not in unique_values:
        unique_values.append(nr)
        unique_number+=1

print(f"There are {unique_number} Unique values and they  are {', '.join(map(str,unique_values))}")