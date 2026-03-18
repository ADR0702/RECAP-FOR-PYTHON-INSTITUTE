# while True:
#     try:
#         user=int(input("Please add a number:\n"))
#         print(f"the number is {user}")
#         break
#     except ValueError:
#         print("You didn't add a number!!")


# def spliticcus():
#     try:
#         user1=int(input("Please add a number:\n"))
#         user2=int(input("Please add a number:\n"))
#         print( user1//user2)
#     except ValueError:
#         print("You didn't add a number!!")
#     except ZeroDivisionError:
#         print("Can't divide with zero!")


# spliticcus()


# while True:
#     try:
#         user=int(input("Please type your age:\n"))
#         if user <= 0:
#             print("Invalid AGE!!")
#         elif user >=18 :
#             print("Adult!")
#             break
#         else:
#             print("Minor!")
#             break
#     except ValueError:
#         print("You didn't add a number!!")

# def mathematics(a, b, operation):
#     while True:
#         operation=input("Please choose the operation:\n +, -, *, //, /, % ")
#         if operation == "+":
#             total= a+b
#             return total
#         elif operation == "-":
#             total= a-b
#             return total
#         elif operation == "*":
#             total= a*b
#             return total
#         elif operation == "//":
#             total= a//b
#             return total
#         elif operation == "/":
#             total= a/b
#             return total
#         elif operation == "%":
#             total= a%b
#             return total
#         else:
#             print("You didn't choosed a the right operation!!")


def minicalculator():
    while True:
        try:
            no1=int(input("Please add your first number:\n"))
            no2=int(input("Please add your second number:\n"))
            operation=input("Please choose the operation:\n +, -, *, //, /, % \n")
            if operation not in "+-*//%/":
                print("You didn't choosed a the right operation!!")
                continue
            if operation == "+":
                total= no1+no2
            elif operation == "-":
                total= no1-no2
            elif operation == "*":
                total= no1*no2
            elif operation == "//":
                total= no1//no2
            elif operation == "/":
                total= no1/no2
            elif operation == "%":
                total= no1%no2

            print(f"the result is {total}")
            break
        except ValueError:
            print("You didn't add a number!!")
        except ZeroDivisionError:
            print("You can't divide with zero!")

    
minicalculator()