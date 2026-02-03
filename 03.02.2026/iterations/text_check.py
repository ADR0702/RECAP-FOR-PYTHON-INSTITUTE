text="banana"
validator=False
for ch in text:
    if ch == "b":
        validator=True

if validator:
    print("yes")
else:
    print("No")
