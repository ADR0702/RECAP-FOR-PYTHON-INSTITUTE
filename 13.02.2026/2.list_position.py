

# nums = [3, 7, 7, 2, 9]
# check=False

# for i in range(len(nums)-1):
#     if nums[i] == nums[i+1]:
#         check=True

# if check:
#     print("Yes!")
# else:
#     print("No!")


# nums = [1, 4, 7, 3, 9]

# breaking_index=-1

# for i in range(len(nums)-1):
#     if nums[i] >= nums[i+1]:
#         breaking_index=i

# print(breaking_index)


# nums = [5, 2, 2, 8, 9]
# count=0

# for i in range(len(nums)-1):
#     if nums[i]== nums[i+1]:
#         count+=1

# if count == 1:
#     print("Yes!")
# else:
#     print("No!")

nums=[4, 7, 7, 7, 2, 9]

counta=False

for i in range(len(nums)-2):
    if nums[i] == nums[i+1] and nums[i] == nums[i+2]:
        counta=True

if counta:
    print("Yes!")
else:
    print("No!")




