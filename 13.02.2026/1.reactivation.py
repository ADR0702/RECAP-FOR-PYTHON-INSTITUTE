nums = [2, 5, 8, 1, 9]

sums=0

for i in nums:
    if i % 2==0:
        sums+=i

print(f"the total amount is :{sums}")

nums = [3, 6, 1, 8, 2]

maxnumber=nums[0]

for i in nums:
    if i > maxnumber:
        maxnumber=i

print(maxnumber)

text = "Ana are 3 mere si 2 pere"
count=0

for i in text:
    if i.isdigit():
        count+=1

print(f"There are {count} digits in the sentence {text}")

nums = [1,2,3,4,5,6]
first_half=[]
for i in range(len(nums)):
    if nums[i] < 4:
        first_half.append(nums[i])

print(first_half)

nums = [1,2,3,4,5,6]
reversed_list=[]

for i in range(len(nums)-1,-1,-1):
    if nums[i] >=4:
        reversed_list.append(nums[i])
print(reversed_list)
    
