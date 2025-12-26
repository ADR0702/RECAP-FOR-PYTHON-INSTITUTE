numbers = [1, 4, 7, 2, 9, 6]
odd_numbers=[]
even_numbers=[]

for j  in numbers:
    if j % 2 == 0:
        even_numbers.append(j)
    else:
        odd_numbers.append(j)

print(f"the odd numbers are {', '.join(map(str, odd_numbers))} and the even numbers are {', '.join(map(str, even_numbers))}")