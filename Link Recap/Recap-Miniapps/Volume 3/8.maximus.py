nums = [3, 7, 2, 9, 4]

biggest = nums[0]          
for no in nums:
    if no > biggest:
        biggest = no       

print(f"The biggest number in the list is {biggest}")