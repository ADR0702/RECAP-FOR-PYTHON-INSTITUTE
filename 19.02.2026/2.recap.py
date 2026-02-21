# # 1
# nums = [3, 10, 5, 8, 1]


# for i in nums:
#     if i >5:
#         print(i)
# # 2
# text = "ana are mere si pere"

# new=text.split()

# for i in new:
#     if len(i) >3:
#         print(i)
# # 3
# preturi = {
#     "mere": 5,
#     "pere": 8,
#     "banane": 4
# }

# for fruit, price in preturi.items():
#     if price >= 5:
#         print(fruit, price)

# # 4
# text="a b a c b a"
# appearances={}

# for ch in text:
#     if ch in appearances:
#         appearances[ch]+=1
#     else:
#         appearances[ch]=1

# print(appearances)

# # 5

# odd_no=[]
# even_no=[]
# while True:
#     user=input("Oy! Douchebag! Insert a number, insert 0 to fuck off:\n")
#     if not user.isdigit():
#         print("You idiot, you didn't insert a number! How Stupid Are You?")
#         continue
#     user=int(user)
#     if user % 2 == 0:
#         even_no.append(user)
#         print("Hey smartass, that's a positive no")
#     else:
#         odd_no.append(user)
#         print("You donnut! that's an odd number!")
#     if user == 0:
#         print("Finally you stopped added useless fucking numbers!")
#         break

# print(f"The worst even numbers saw in my life are: {even_no}")
# print(f"The worst odd numbers saw in my life are: {odd_no}")
# print("The program thanks you for being an idiot and wishes you to fuck off!")


# vowels = "aeiouAEIOU"
# vowels_no=0
# vowels_typed=[]        
# text=input("Add a text!\n")
     
# for i in text:
#     if i in vowels:
#         vowels_no+=1
#         vowels_typed.append(i)
# print(f"the total vowels are : {vowels_no} ") 
# print(f"the vowels are {",".join( vowels_typed)}")

for i in range(5):
    if i == 3:
        break
    if i == 1:
        continue
    print(i)

