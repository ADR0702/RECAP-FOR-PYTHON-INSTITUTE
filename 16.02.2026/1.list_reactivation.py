# nums = [5, 3, 8, 2, 9, 1]
# check=False
# for i in range(len(nums)-2):
#     if nums[i]> nums[i+2]:
#         check=True

# if check:
#     print("yes!")
# else:
#     print("No!")

nums = [1, 2, 3, 4, 1, 2, 3]

check=False

for i in range(len(nums)-3):
    if nums[i] < nums[i+1] and nums[i+1] < nums[i+2] and nums[i+2] < nums[i+3]:
        check=True

if check:
    print("yes they are one crescendo!")
else:
    print("No!")
        