import random

random_characters="afsfdajsnkjnfkdnasljdnal"
choosed_characters=[]
choosed_characters+=random.choices(random_characters, k=6)
print(choosed_characters)
string_of_choosed_characters="-".join(choosed_characters)

print(string_of_choosed_characters)