text = input("type down a word:\n")
vowels_list=["a","e","i","o","u"]

vowels=[]

consonants=[]
for ch in text:
    if ch.isalpha():
        if ch in vowels_list:
            vowels.append(ch)
        else:
            consonants.append(ch)
           
print(f"Vowels: {vowels} ({len(vowels)})")
print(f"Consonants: {consonants} ({len(consonants)})")
