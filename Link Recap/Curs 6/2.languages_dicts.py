translates={
    "ro": {
        "no1":"Introduceți primul număr\n", 
        "numeric": "Introduceti doar numere!!\n",
        "no2":"Introduceți al 2-lea număr\n", 
        "op": "Alegeți operația +, -, *, /\n",
        "re_op": "Alegeti doar din +, -, *, / \n",
        "rez": "rezultatul este:",
    },
    "en": {
        "no1": "Enter the first number\n",
        "numeric": "Enter numbers only!!\n",
        "no2": "Enter the second number\n",
        "op": "Choose the operation +, -, *, /\n",
        "re_op": "Choose only from +, -, *, /\n",
        "rez": "the result is:",
    },
    "it":{
        "no1": "Inserisci il primo numero\n",
        "numeric": "Inserisci solo numeri!!\n",
        "no2": "Inserisci il secondo numero\n",
        "op": "Scegli l'operazione +, -, *, /\n",
        "re_op": "Scegli solo tra +, -, *, /\n",
        "rez": "il risultato è:",
    },
    "fr":{
        "no1": "Entrez le premier nombre\n",
        "numeric": "Entrez seulement des nombres !!\n",
        "no2": "Entrez le deuxième nombre\n",
        "op": "Choisissez l'opération (+, -, *, /)\n",
        "re_op": "Choisissez seulement parmi +, -, *, /\n",
        "rez": "le résultat est :",
    },
    "de":{
        "no1": "Geben Sie die erste Zahl ein\n",
        "numeric": "Bitte nur Zahlen eingeben!!\n",
        "no2": "Geben Sie die zweite Zahl ein\n",
        "op": "Wählen Sie die Operation +, -, *, /\n",
        "re_op": "Wählen Sie nur aus +, -, *, /\n",
        "rez": "das Ergebnis ist",
    }
}

lang=input(f"Please Choose from {list(translates.keys())}\n")

while lang not in translates.keys():
    lang=input(f"Please Choose from {list(translates.keys())}\n")

no1=(input(translates[lang]["no1"]))
while not no1.isnumeric():
    no1=(input(translates[lang]["numeric"]))
no1=int(no1)
print(no1)

no2=(input(translates[lang]["no2"]))
while not no2.isnumeric():
    no2=(input(translates[lang]["numeric"]))
no2=int(no2)
print(no2)

op=input(translates[lang]["op"])
while op not in ("+", "-", "*", "/"):
    op=input(translates[lang]["re_op"])

if op=="+":
    result=no1+no2
elif op=="-":
    result=no1-no2
elif op=="*":
    result=no1*no2
elif op=="/":
    result=no1/no2

print(translates[lang]["rez"], result)
