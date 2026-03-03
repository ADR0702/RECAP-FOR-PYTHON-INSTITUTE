

def nosum(a, b):
    return(a + b)
def nominus(a, b):
    return(a - b)
def nomultiply(a, b):
    return(a * b)
def nodivide(a, b):
    if b == 0:
        return("Can't divide 0")
    return(a / b)
def nofloor(a, b):
    if b == 0:
        return("Can't // 0")
    return(a // b)
def nomodulo(a, b):
    if b == 0:
        return("Can't % 0")
    return(a % b)
def nopower(a, b):
    return(a ** b)

def menu():
    print("1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Floor Division")
    print("6.Modulo")
    print("7.Power")

print("Wellcome to the math app! Please choose your operation, choose 0 to stop the app:")

while True:
    menu()
    choice=int(input("Type:"))
    if choice == 0:
        print("Thank you for choosing our app! i hope it helped!")
        break
    elif choice > 7:
        print("Invalid option!!\n")
    else:
        first=int(input("First number:"))
        second=int(input("Second number:"))
        if choice == 1:
            print(f"the result is: {nosum(first, second)}!")
        elif choice == 2:
            print(f"the result is:{nominus(first, second)}!")
        elif choice == 3:
            print(f"the result is:{nomultiply(first, second)}!")
        elif choice == 4:
            print(f"the result is:{nodivide(first, second)}!")
        elif choice == 5:
            print(f"the result is:{nofloor(first, second)}!")
        elif choice == 6:
            print(f"the result is:{nomodulo(first, second)}!")
        elif choice == 7:
            print(f"the result is:{nopower(first, second)}!")
        else:
            print("You didn't add an invalid option")
        

