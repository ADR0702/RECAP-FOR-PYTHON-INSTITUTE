student = {
    "nume": "Ion",
    "varsta": 21,
    "oras": "Bucuresti"
}

print(student["varsta"], student["oras"])

student["facultate"]="Universitatea Romano-Americana"
student["varsta"]=22

produse = {
    "mere": 5,
    "pere": 8,
    "banane": 4,
    "portocale": 10
}

for produs, pret in produse.items():
    if pret > 8:
        print(produs, pret)

        
