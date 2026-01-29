nums = [1, 2, 3, 4, 5]
reversed_nums=[]

for no in range(len(nums)-1,-1,-1):
    reversed_nums.append(nums[no])

print(reversed_nums)