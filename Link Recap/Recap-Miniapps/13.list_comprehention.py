# numbers = [1,2,3,4,5]
# squares = []
# for n in numbers:
#     square = n**2
#     squares.append(square)
# print(squares)


# simplified:
# numbers = [1,2,3,4,5]
# squares=[n**2 for n in numbers ]
# print(squares)


# numbers=[1,2,3,4,5,6,7,8,9,10]
# new_list=[n**2 for n in numbers if n %2==0]
# print(new_list)

# numbers=[1,2,3,4,5,6,7,8,9,10]
# new_list=[n**2 for n in numbers if not n %2==0]
# print(new_list)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# ch_no=[len(n) for n in fruits if len(n) > 4]

# print(ch_no)

# numbers=list(range(1,21))
# square_numbers=[n for n in numbers if n % 4==0]


# print(square_numbers)

words = ["hello", "world", "python", "code"]

new_list=[w[:3] for w in words]


print(new_list)