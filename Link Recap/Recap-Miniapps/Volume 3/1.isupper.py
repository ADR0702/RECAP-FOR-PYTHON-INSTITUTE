text=input('Please add a random text:\n')
count=0
for i in text:
    if i.isupper():
        count+=1
print(f'the number uppercase letters is :{count}')