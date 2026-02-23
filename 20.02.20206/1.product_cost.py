products = {
    "laptop": 3500,
    "mouse": 150,
    "keyboard": 400,
    "monitor": 1200
}
total=0
expensive={}
for item, value in products.items():
    if value > 1000:
        total+=value
        expensive[item]=value

print(f"The products that costs more than 1000 Euro {", ".join(expensive)} \n Their total amount is {total} Euro")



            




    

