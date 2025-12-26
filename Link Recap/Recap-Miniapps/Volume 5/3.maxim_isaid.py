values = [6, 2, 9, 4, 7]

maximum_value=values[0]

for nr in values:
    if nr > maximum_value:
        maximum_value=nr

print(f"The biggest value in the list is {maximum_value}")