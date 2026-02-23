money_spender={}
total=0
biggest_spent=""
biggest_value=0


while True:
    expense=input("Please add your monthly expence or type stop to end the program:\n")
    if expense== "stop":
        break
    amount=float(input("Please add the amount spent:\n"))
    if expense in money_spender:
        money_spender[expense]+=amount
    else:
        money_spender[expense]=amount

    total+=amount

    if money_spender[expense] > biggest_value:
        biggest_value = money_spender[expense]
        biggest_spent = expense

print(f"All monthly spendings are: {money_spender}")
print(f"The total amount of spendings are: {total}")
print(f"The biggest monthly spending is:{biggest_spent} with the amount of {biggest_value} RON")
print("Thank you!")


    
       