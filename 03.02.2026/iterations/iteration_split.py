nums = [1, 2, 3, 4, 5, 6]

for x in range(len(nums)//2):
    print(f"first half:{nums[x]}")

for x in range(len(nums) //2, len(nums)):
    print(f"second half:{nums[x]}")


for i in range(4, 0, -1):
    print(i)