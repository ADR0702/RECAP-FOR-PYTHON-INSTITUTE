nums = [7, 3, 9, 2, 8]
smallest=nums[0]


for nr in nums:
    if nr < smallest:
        smallest=nr

print(f"the smallest number from {nums} is {smallest}")
