# numbers = [3, 5, 3, 7, 5, 9, 3]
# new_list=[]

# for no in range(len(numbers)):
#     if numbers[no] not in new_list:
#         new_list.append(numbers[no])
        

# print(new_list)


text = "Ana are 2 mere si 3 pere"
new_text=text.split()
requested_text=[]

for word in new_text:
    if not word.isdigit():
        requested_text.append(word)

new_requested_text=' '.join(requested_text)

print(new_requested_text.strip())