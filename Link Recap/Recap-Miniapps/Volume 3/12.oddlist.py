nums = [3, 5, 7, 8, 9, 10]
oddno=0

for ch in nums:
    if ch % 2==0:
        oddno=ch
        break

print(oddno)