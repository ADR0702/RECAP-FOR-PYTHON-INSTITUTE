text = "Ana are 2 mere si 3 pere"
count=0

for i in text:
    if i.isdigit():
        count+=1
print(f"there are {count} numbers in the string text")
