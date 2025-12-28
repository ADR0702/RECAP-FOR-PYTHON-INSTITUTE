nums = [7, 3, 9, 2, 8]
smallest_no=nums[0]
biggest_no=nums[0]

for nr in nums:
    if nr < smallest_no:
        smallest_no=nr
    elif nr>biggest_no:
        biggest_no=nr

print(f"the smallest number is {smallest_no} and the biggest number is {biggest_no}")