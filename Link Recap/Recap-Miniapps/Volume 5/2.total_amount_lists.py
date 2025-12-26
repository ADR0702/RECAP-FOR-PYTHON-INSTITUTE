numbers = [2, 5, 8, 3, 10]
odd_numbers=[]
total_amount=0

for j in numbers:
    if j % 2==0:
        odd_numbers.append(j)
        total_amount+=j

print(f"the odd numbers are {' '.join(map(str,odd_numbers))} and the total amount is {total_amount}")
