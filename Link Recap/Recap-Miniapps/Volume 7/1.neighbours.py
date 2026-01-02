nums = [10, 7, 5, 8, 6]
absolut_no=[]

for i in range(len(nums)-1):
    d= nums[i] - nums[i+1]
    if d < 0:
        d=-d
    absolut_no.append(d)

print(f"The absolut list is {absolut_no}")
