tari=["ro", "en", "de", "ar" "it", "hu", "es","pt", "gr", "fr", "is"]
greetings=["Salut", "Hello", "Hallo", "Marhaba", "Ciao", "Szia", "Ola","Ola", "Bonjour", "Shalom",]

countries_nd_greetings={}

for i in range(len(tari)):
    countries_nd_greetings [tari[i]]=greetings[i]
print(countries_nd_greetings)
