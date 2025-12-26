numbers = [3, 10, 5, 8, 2]
total_amount=0

for nr in numbers:
    if nr >= 5:
        total_amount+=nr

print(f"the total amount for numbers in the list bigger or equal than 5 is: {total_amount}")