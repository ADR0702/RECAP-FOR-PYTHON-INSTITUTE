text=input("Please write a word:\n")
count=0

for ch in text:
    if ch.islower():
        count+=1

print(f"the number of small characters in the word {text} are {count}")