#1.
text = "HeLLo"
print(text.lower())
# 2.
text = "123a"
digits=True

for ch in text:
    if not ch.isdigit():
        digits=False

if digits:
    print("Yes")
else:
    print("no")

#3.
text = "Ana are 2 mere si 3 pere"
count=0
for ch in text:
    if ch.isdigit():
        count+=1
print(f"there are {count} digits in the text")

# 4.
text = "Ana are mere"
letters=0
spaces=0

for ch in text:
    if ch.isalpha():
        letters+=1
    elif ch.isspace():
        spaces+=1
print(f"there are {letters} letters in the text and {spaces} spaces")