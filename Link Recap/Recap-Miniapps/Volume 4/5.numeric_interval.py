# user_number=input("Please type a number:\n")
# user_number=int(user_number)

# if user_number in range(10, 21):
#     print('Interior')
# else:
#     print("Exterior") 

# user_number=int(input("Please type a number:\n"))


# if user_number % 2 == 0:
#     print("Even")
# else:
#     print("odd")

# user_number=int(input("Please type a number from 0 10:\n"))

# if user_number < 0 or user_number > 10:
#     print("invalid number")
# else:
#     print("Valid Number")

# user_number=int(input("Please type a number from 0 10:\n"))

# if not user_number > 0:
#     print("Not Positive")
# else:
#     print("Positive")

# user_number=int(input("Please type a number from 0 10:\n"))
# if user_number in range(5,101):
#     print("Accepted")
# else:
#     print("Rejected")

# numbers = [1, 2, 3]
# print(sum(numbers))
# numbers = [10, 20, 30]

# numbers.append(40)
# numbers.append(50)

# print(numbers)

# values = [1, 2, 3]
# total = 0

# for v in values:
#     total = total + values

# print(total)
# items = ["a", "b", "c"]

# items[1] = "x"

# print(items)

# nums = [5, 10, 15]

# if nums[0] + nums[1] == nums[2]:
#     print("True")
# else:
#     print("false")

# numbers = [2, 4, 6, 8]

# total=0

# for i in numbers:
#     total+=i

# print(total)

# values = [1, 5, 8, 2, 9]

# big_values=0

# for i in values:
#     if i > values[1]:
#         big_values+=1

# print(big_values)

# numbers = [7, 3, 10, 2, 8]

# biggest_number=0

# for i in numbers:
#     if i >= numbers[2]:
#         biggest_number=i

# print(biggest_number)

nums = [3, 6, 9, 12]

odd_numbers=[]

for i in nums:
    if i % 2==0:
        odd_numbers.append(i)

print(odd_numbers)
