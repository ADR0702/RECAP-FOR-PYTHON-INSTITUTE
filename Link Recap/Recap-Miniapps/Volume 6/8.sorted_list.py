nums = [1, 7, 3, 5, 4, 8]
ascending=True

for i in range(len(nums)-1):
    if nums[i] >= nums[i+1]:
        ascending=False

if ascending:
    print('ascending')
else:
    print('not ascending')

