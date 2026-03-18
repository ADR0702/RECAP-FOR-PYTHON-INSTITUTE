def get_number():
    while True:
        try:
            no=int(input("Please type a valid number:\n"))
            return no
        except ValueError:
            print("Not a number!")

def mthm():
    while True:
        try:
            no1=get_number()
            no2=get_number()
            operation=input("Please choose the operation:    +, -, *, /, \n")
            if operation not in ["+", "-", "*", "/"]:
                print("You didn't choosed a the right operation!!")
                continue
            if operation == "+":
                total= no1+no2
            elif operation == "-":
                total= no1-no2
            elif operation == "*":
                total= no1*no2
            elif operation == "/":
                total= no1/no2
            print(f"the result is {total}")
            break
        except ZeroDivisionError:
            print("Zerro Divison Error!")

mthm()