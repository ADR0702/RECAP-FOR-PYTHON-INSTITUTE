values = [3, 10, 15, 2, 8]
the_numbers=[]
the_amount_of_numbers=0

for nr in values:
    if nr >=5  and nr <=10:
        the_numbers.append(nr)
        the_amount_of_numbers+=1

print(f"The numbers are: {' '.join(map(str,the_numbers))} and the amount of the numbers are {the_amount_of_numbers}")