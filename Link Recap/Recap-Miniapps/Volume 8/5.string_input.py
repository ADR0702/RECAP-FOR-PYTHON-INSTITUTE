#1.
name=input("please add a name\n")

if name.isalpha():
    print("Ok")
else:
    print("invalid")
#2.
age=input("please add your age\n")

if age.isdigit():
    print("Ok")
else:
    print("invalid")
#3.
password=input("please add a password:\n")

if len(password)>=6:
    print("Password Good")
else:
    print("password too short")

# 4.
text=input("please add a random text:\n")
count=0

for ch in text:
    if ch.isdigit():
        count+=1
print(count)

