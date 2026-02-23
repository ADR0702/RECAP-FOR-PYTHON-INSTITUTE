text="apple banana apple orange banana apple"
new_text=text.split()
basket={}
fruit_counter=0
frequent_fruit=""
for fruit in new_text:
    if fruit in basket:
        basket[fruit]+=1
    else:
        basket[fruit]=1
for fruit, count in basket.items():
    if count > fruit_counter:
        fruit_counter=count
        frequent_fruit=fruit

print(f"There are {fruit_counter} {frequent_fruit} in the basket")


