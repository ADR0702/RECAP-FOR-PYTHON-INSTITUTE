nums = [3, 8, 7, 2, 9]
equal=0
for i in range(len(nums)-1):
    if nums[i]==nums[i+1]:
        equal=1

if equal == 1:
    print("Yes!")
else:
    print("No!")
