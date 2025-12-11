numbers = [1, 4, 7, 9, 12, 15, 20]
print(type(numbers))
odd_numbers=[]
even_numbers=[]

for i in numbers:
    if i % 2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
        
print(odd_numbers)
print(even_numbers)