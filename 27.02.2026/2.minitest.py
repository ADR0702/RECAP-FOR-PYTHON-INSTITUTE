# 1.
grades = {
    "ana": 9,
    "ion": 7,
    "maria": 10,
    "paul": 8
}
total=0
bgr=0
brilliant=""
for student, gr in grades.items():
    total+=gr
    if gr > bgr:
        bgr=gr
        brilliant=student

media=total/len(grades)

print(f"the average grade of the class is {media}")
print(f"the most briliant student in the class is {brilliant} with the score {bgr}")

# 2
club1 = ["ana", "ion", "paul", "maria", "ion"]
club2 = ["george", "paul", "alex", "ana"]

club1=set(club1)
club2=set(club2)

print(club1 | club2)
print(club1 & club2)
print(club1 ^ club2)

# 3
nums = [5, 12, 3, 19, 7, 2]
start=0
count=0
for no in nums:
    if no > 10:
        count+=1
    if no > start:
        start=no
    
print(f"there are {count} numbers bigger than 10")
print(f"the biggest number is {start}")

# 4
text = "python is fun python is powerful python"
new_text=text.split()
dictext={}
for word in new_text:
    if word in dictext:
        dictext[word]+=1
    else:
        dictext[word]=1

print(f"each word appears in following order: {dictext} ")

frq=0
frqw=""
for wrd, cnt in dictext.items():
    if cnt > frq:
        frq=cnt
        frqw=wrd
print(f'the most frequent word in " {text}" is {frqw} with {frq} appearences ')