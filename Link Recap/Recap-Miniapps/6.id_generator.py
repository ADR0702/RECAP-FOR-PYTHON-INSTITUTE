import random
import string

def id_generator():
    user=int(input("Please type how many id's you want to generate:\n"))
    special_list="!@#$%^&*"
    list_id=[]

    for _ in range(user):
        
        ids=""
        ids+=''.join(random.choices(string.ascii_letters, k=2))
        ids+=random.choice(special_list)
        ids+=''.join(random.choices(string.digits, k=4))
        list_id.append(ids)
        
    print(', '.join(list_id))      

id_generator()