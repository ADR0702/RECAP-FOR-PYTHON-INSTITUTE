# 1.
user=input("Please type any word:\n")

if len(user) <4:
    print("Short word")
elif len(user) > 7:
    print("Long word!")
else:
    print("Medium word")

# 2.
nums = [3, 10, 7, 2, 8, 1]
nums2=[]

for i in nums:
    if i > 5:
        nums2.append(i)
print(nums2)

# 3
while True:
    user_number=input("Please add any number, press 0 to stop:\n")
    if not user_number.isdigit():
        print("Please enter a valid number!")
        continue
    if user_number=="0":
        print("program stopped")
        break


# 4

text = "Ana are 3 mere si 12 pere"

for i in text:
    if i.isdigit():
        print(i)




    



