nums = [7, 3, 9, 2, 8]
smallest=nums[0]

for i in nums:
    if i < smallest:
        smallest=i


print(f"the smallest number in the list is {smallest}")
    