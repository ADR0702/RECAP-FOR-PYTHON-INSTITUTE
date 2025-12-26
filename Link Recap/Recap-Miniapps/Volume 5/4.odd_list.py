nums = [1, 4, 6, 9]
odd_list=[]

for nr in nums:
    if not nr % 2==0:
        odd_list.append(nr)


print(f"the odd list of numbers are {" ".join(map(str, odd_list))}")
