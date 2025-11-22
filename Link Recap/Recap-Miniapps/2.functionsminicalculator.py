
operations=["+", "-", "*", "/", "//", "%"]


def numeric_check(user):
    while  not user.isnumeric():
        user=(input("Please add a number:\n"))
    return user


def mathematics(no1, no2, operation):
    if operation == "+":
        return no1+no2
    elif operation == "-":
        return no1-no2
    elif operation == "*":
        return no1*no2
    elif operation == "/":
        return no1/no2
    elif operation == "//":
        return no1//no2
    elif operation == "%":
        return no1%no2
    

first_number=(input("Please Add first number:\n"))
second_number=(input("Please Add second number:\n"))

first_number=numeric_check(first_number)
second_number=numeric_check(second_number)
first_number=int(first_number)
second_number=int(second_number)

operation=input("Please choose operation: + , - , * , / , // , %\n")
while operation not in operations:
      print("Please choose the options i gave you!")
      operation=input("Please choose operation: + , - , * , / , // , % \n")


result=mathematics(first_number, second_number, operation)

print(f"The result of {first_number} {operation} {second_number} is {result}")






