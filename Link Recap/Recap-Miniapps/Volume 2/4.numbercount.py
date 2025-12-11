word=input("Please add a word, any word:\n")
count=0
for i in word:
    if i.isdigit():
        count+=1

print(f"the word {word} has {count} numbers")
