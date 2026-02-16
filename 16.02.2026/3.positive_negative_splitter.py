# positive_no=[]
# negative_no=[]
# while True:
#     user_no=input("Please add any number: \n")
#     try:
#         user_no=int(user_no)
#     except ValueError:
#         print("invalid number")
#         continue
#     if user_no > 0:
#         positive_no.append(user_no)
#         print(f"The Number {user_no} is a positive number ")

#     elif user_no < 0:
#         negative_no.append(user_no)
#         print(f"The Number {user_no} is a negative number ")

#     else:
#         print(f"the positive numbers are: {" ,".join(map(str, positive_no))}")
#         print(f"the negative numbers are: {" ,".join(map(str, negative_no))}")
#         print("Program Stopped!")
#         break

d = {}

for cuv in ["ana", "are", "ana"]:
    if cuv in d:
        d[cuv] += 1
    else:
        d[cuv] = 1

print(d)