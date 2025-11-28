numbers = [1,2,3,4,5]
squares = []
for n in numbers:
    square = n**2
    squares.append(square)
print(squares)


# simplified:
numbers = [1,2,3,4,5]
squares=[n**2 for n in numbers ]
print(squares)


numbers=[1,2,3,4,5,6,7,8,9,10]
new_list=[n**2 for n in numbers if n %2==0]
print(new_list)