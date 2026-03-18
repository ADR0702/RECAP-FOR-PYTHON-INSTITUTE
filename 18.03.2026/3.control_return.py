def get_number():
    while True:
        try:
            no=int(input("Please type a valid number:\n"))
            return no
        except ValueError:
            print("Not a number!")
        

a=get_number()
b=get_number()
total=a+b

print(f"the sum of {a} and {b} is {total}")


def divide(a, b):
        try:
            return a/b   
        except ZeroDivisionError:
            print("Error")
            
        
print(divide(180, 0))



# 9




def mthm(no1, no2, operation):
    while True:
        try:
            no1=get_number()
            no2=get_number()
            operation=input("Please choose the operation:\n +, -, *, //, /, % ")
            if operation not in "+-*//%/":
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
            print("Error!")





