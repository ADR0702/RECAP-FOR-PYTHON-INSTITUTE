lang=input("Please Choose from (ro/en/it)\n")

while lang not in ('ro', "en", "it"):
    lang=input("Please Choose from (ro/en/it)\n")
translations={
    "ro": ("Introduceți primul număr", "Introduceți al 2-lea număr", "Alegeți operația (+, -, *, /)", "rezultatul este:"),
    "en":("Enter the first number", "Enter the second number", "Choose the operation (+, -, *, /)", "the result is:"),
    "it": ("Inserisci il primo numero", "Inserisci il secondo numero", "Scegli l'operazione (+, -, *,/)", "Is Resultato e:"),
}

no1=int(input(translations[lang][0]))
print(no1)

no2=int(input(translations[lang][1]))
print(no2)

op=input(translations[lang][2])

result=no1+no2
print(translations[lang][2], result)

