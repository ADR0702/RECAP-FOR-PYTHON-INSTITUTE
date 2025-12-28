numbers = [3, 10, 5, 8, 2]
nr_even=[]
nr_sum=0
nr_count=0

for nr in numbers:
    if nr % 2 == 0:
        nr_even.append(nr)
        nr_sum+=nr
        nr_count+=1

print(f"There are {nr_count} even numbers, they are {', '.join(map(str, nr_even))} and the total sum is {nr_sum} ")