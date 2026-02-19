# note = {
#     "Ana": 9,
#     "Ion": 7,
#     "Maria": 10
# }

# for key, grades in note.items():
#     if grades == 9:
#         print(key, grades)

# masina = {
#     "marca": "Dacia",
#     "an": 2018
# }

# masina["culoare"]="alb"

# print(masina)

# text = "mere pere mere banane mere"
# cuvinte=text.split()

# aparitii={}

# for cuv in cuvinte:
#     if cuv in aparitii:
#         aparitii[cuv]+=1
#     else:
#         aparitii[cuv]=1

# print(aparitii)


# fructe = ["mere", "pere", "banane"]
# dictionary={}

# for i, fruit in enumerate(fructe):
#     dictionary[i]=fruit

# print(dictionary)

# cuvinte = ["ana", "programare", "python"]
# d={}

# for i in cuvinte:
#     d[i]=len(cuvinte)

# print(d)

nume = ["Ana", "Ion", "Maria"]
note = [9, 7, 10]

catalog = {}

for i in range(len(nume)):
    catalog[nume[i]] = note[i]

print(catalog)



nume = ["Ana", "Ion", "Maria"]

dic={}

for i in range(len(nume)):
    dic[i]=len[i]

print(dic)