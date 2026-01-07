
text = "Python"


print(text[0], text[5])


word = "abcde"

for ch in range(len(word)):
    print(ch, word[ch])


text = "Hello"
count=0

for ch in text:
  count+=1
print(f"There are {count} letters in the word {text}")

text = "Ana are mere"
count=0

for ch in text:
    if ch == " ":
        count+=1
print(f"There are {count} spaces in the phrase {text}")