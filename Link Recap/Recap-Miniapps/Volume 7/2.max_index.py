nums = [4, 9, 2, 9, 1]
max_number=nums[0]
max_index=0

for i in range(1, len(nums)):
    if nums[i] > max_index:
        max_number=nums[i]
        max_index=i

print(f"The biggest number from the list is {max_number}, at the index { max_index}")