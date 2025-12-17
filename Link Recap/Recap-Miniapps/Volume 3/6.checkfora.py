word=input("Please type a word:\n")
a=False
for ch in word:
    if ch == "a":
        a=True
        break
if a == True:
    print("Found it")
else:
    print("Not Found it")


