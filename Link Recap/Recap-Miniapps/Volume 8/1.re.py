nums = [1, 2, 3]

for j in nums:
    print(j * 2)

nums = [2, 4, 6]
total=0

for j in nums:
    total+=j
print(total)

nums = [1, 5, 8, 2, 9]
count=0

for j in nums:
    if j > 5:
        count+=1

print(f"there are {count} numbers bigger than 5")

nums = [1, 4, 6, 9]
even=[]
odd=[]

for j in nums:
    if j % 2 == 0:
        even.append(j)
    else:
        odd.append(j)
print(f"even numbers are {', '.join(map(str,even))} and odd numbers are {', '.join(map(str,odd))}")

nums = [3, 7, 2, 9]
biggest=nums[0]

for j in nums:
    if j > biggest:
        biggest=j

print(biggest)


nums = [10, 20, 30]

for j in range(len(nums)):
    print(j, nums[j])

nums = [3, 5, 5, 2]
identifier=False
for j in range(len(nums)-1):
    if nums[j]==nums[j + 1]:
        identifier=True

if identifier==True:
    print("Yes")
else:
    print("No")

nums = [1, 3, 5, 7]
rising=True

for j in range(len(nums)-1):
    if nums[j] >= nums[j+1]:
        rising=False

if rising:
    print("yes")
else:
    print("no")

nums = [1, 2, 3, 4]
reversed_list=[]

for j in range(len(nums)-1, -1, -1):
    reversed_list.append(nums[j])

print(reversed_list)


nums = [10, 20, 30]
reversed_list=[]

for j in range(len(nums)-1,-1,-1):
    reversed_list.append(nums[j])

print(reversed_list)

for i in range(10):
    print(i, i+1)