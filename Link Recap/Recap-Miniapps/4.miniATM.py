

def compliance_check():
    while True:
        pin=input("Please add 4 digit numbers pin:\n")
        if len(pin) != 4:
            print("The pin must be 4 digit numbers! try again!\n")
            continue
        if not pin.isnumeric():
            print("You didn't add numbers!")
            continue
        return int(pin)

bank_pin=4827
contor=0

while contor < 3:
    client_pin=compliance_check()
    if client_pin != bank_pin:
        contor+=1
        print(f"Wrong Pin! Please try Again! Attempt {contor}/3")
        if contor == 3:
            print("The pin entered is wrong, the account is blocked, please contact the bank!")
            break
    else:
        print("Acces Granted!")
        break


def bank_transactions(client_sold):
    while True:
        operations=input("Choose operations:\n withdraw amount \n deposit amount \n check current sold\n exit\n")
        if operations == "withdraw amount":
            withdraw_operation=int(input("Please add the amount you wish to withdraw:\n"))
            while withdraw_operation>client_sold:
                withdraw_operation=int(input("The amount requested is over the current sold, Please add the amount you wish to withdraw:\n "))
            new_clientsold=client_sold-withdraw_operation
            print(f"Transaction Succeded! Current Sold:{new_clientsold} RON")
            client_sold=new_clientsold
        elif operations == "deposit amount":
            deposit_amount=int(input("Please add the amount you want to deposit:\n"))
            new_clientsold=client_sold+deposit_amount
            print(f"The new current sold is: {new_clientsold} RON")
            client_sold=new_clientsold
        elif operations == "check current sold":
            print(f"Your current sold is : {client_sold} RON") 
        elif operations == "exit":
            print("Thank you!")
            break   

bank_transactions(450_000)
                

