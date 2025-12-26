nums = [4, 7, 1, 9, 3]
bigger_five=0
list_nums=[]


for nr in nums:
    if nr > 5:
        bigger_five+=1
        list_nums.append(nr)

print(f"There are {bigger_five} bigger numbers than 5 and they are {list_nums}")
