text=input("Please write a text:\n")
new_text=""

for ch in text:
    if not ch.isspace():
        new_text+=ch

print(new_text)
