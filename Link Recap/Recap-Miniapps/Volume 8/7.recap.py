nums = [1, 3, 5, 7]
total=0
for j in nums:
    total+=j
print(total)


text = "Ana are 2 mere si 3 pere"
digits=0

for j in text:
    if j.isdigit():
        digits+=1

print(f"There are {digits} digits in the phrase: {text}")


text=input("Please add a text\n")
value=True

for j in text:
    if not j.isalpha():
        value=False
if value:
    print("Valid")
else:
    print("invalid")


nums = [4, 6, 6, 1]
count=0

for j in range(len(nums)-1):
    if nums[j]==nums[j+1]:
        count=1

if count >0:
    print("Da")
else:
    print("Nu")


nums = [10,20,30]
reversed_nums=[]

for j in range(len(nums)-1,-1,-1):
    reversed_nums.append(nums[j])  

print(reversed_nums)     