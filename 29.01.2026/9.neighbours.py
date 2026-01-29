nums = [1, 2, 3, 2, 5]
neighbours_no=0

for no in range(len(nums)-1):
    if nums[no]==nums[no+1]:
        neighbours_no+=1

if neighbours_no==1:
    print("yes!")
else:
    print("No")