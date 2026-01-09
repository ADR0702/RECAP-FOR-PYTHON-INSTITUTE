text = "Ana are foarte multe mere rosii"
split_text=text.split()
counter=0
big_words=[]

for cuv in split_text:
    if len(cuv) >=5:
        counter+=1
        big_words.append(cuv)

print(f"there are {counter} words that have more than 5 characters and they are: {", ".join(big_words)}")


text = "Ana are Mere Rosii si Pere"
split_text=text.split()
upper_words=[]
for word in split_text:
    if word[0].isupper():
        upper_words.append(word)


print(upper_words)

text = "Ana are 2 mere si 3pere rosii"
split_text=text.split()
new_text=[]

for word in split_text:
    if word.isalpha():
        new_text.append(word)

print(' '.join(new_text))

text = "Ana are mere si pere"
split_text=text.split()
new_text=[]
for cuv in split_text:
    if len(cuv)<3:
        cuv="***"
    new_text.append(cuv)

print(' '.join(new_text))

opt=int(input("Please add a number from 1 to 3:\n"))
if opt >= 1 and opt <=3:
    print("ok")
else:
    print("Invalid")

i = 0
while i < 5:
    print(i)
    i += 1