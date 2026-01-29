text = "Ana are foarte multe mere rosii"
words= text.split()
print(words)
result=[]

for i in words:
    if len(i) >=4:
        result.append(i)

final_text=" ".join(result)
print(final_text)

