# text = "Ana are mere."
# text = text.replace(".", "")
# print(text)

# value = input("Number: ")

# if value.replace(".", "", 1).isdigit():
#     value = float(value)
# else:
#     print("Invalid number")


user_text=input("Please add a text:").strip().lower()

user_text=user_text.replace(".", " ")
user_text=user_text.replace(",", " ")
user_text=user_text.replace("!", " ")
user_text=user_text.replace("?", " ")

new_text=user_text.split()
counting=0
pythoncount=0
longest_word=""

for word in new_text:
    counting+=1
    if word=="python":
        pythoncount+=1
    if len(word) > len(longest_word):
        longest_word=word

print(f"the total number of words the text are {counting}")
print(f"the longest word is {longest_word}")  
print(f"'python' appears {pythoncount} times")
if user_text.startswith("python"):
    print("Yes! the text starts with the word Python")
else:
    print("No! the text doesn't starts with the word Python")
    
