text = "Ana are foarte multe mere rosii"

textlist=text.split()
new_text_list=[]

for i in textlist:
    if not i[0].isupper():
        new_text_list.append(i)
        

new_text=" ".join(new_text_list)
print(new_text)