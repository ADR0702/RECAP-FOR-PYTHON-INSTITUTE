
text = "Ana are mere rosii"
words=text.split()
count=0
for j in words:
    count+=1

print(f"there are {count} words in the text:{text}")



text = "Invat Python zilnic"
words=text.split()

for j in words:
    print(j)

text = "Ana are mere"
words=text.split()
print(words)
reversed_list=[]
for j in range(len(words)-1,-1,-1):
    reversed_list.append(words[j])

print(" ".join(reversed_list))


text = "Ana are foarte multe mere"
new_text=text.split()
print(new_text)
final_text=[]
for cuv in new_text:
    if len(cuv) >= 4:
        final_text.append(cuv)

print(" ".join(final_text))

            

