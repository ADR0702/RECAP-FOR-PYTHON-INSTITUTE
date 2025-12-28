values = [1, 6, 9, 12, 4, 7]
odd_bigger=[]
odd_sum=0
odd_total_nr=0

for nr in values:
    if nr % 2 !=0 and nr >=5:
        odd_bigger.append(nr)
        odd_total_nr+=1
        odd_sum+=nr
        

print(f"the total odd numbers bigger than 5 are {odd_total_nr}, they are {', '.join(map(str,odd_bigger))} and sum of them is {odd_sum}")