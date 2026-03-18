import math

while True:
    no=input("please add a random number:")
    if not no.isdigit():
        print("i said a number not a character!!!")
        continue
    else:
        no=int(no)
        break
radical_no=math.sqrt(no)
print(radical_no)








