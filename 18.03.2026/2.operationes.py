 operation=input("Please choose the operation:\n +, -, *, //, /, % ")
            if operation == "+":
                total= no1+no2
                return total
            elif operation == "-":
                total= no1-no2
                return total
            elif operation == "*":
                total= no1*no2
                return total
            elif operation == "//":
                total= no1//no2
                return total
            elif operation == "/":
                total= no1/no2
                return total
            elif operation == "%":
                total= no1%no2
                return total
            else:
                print("You didn't choosed a the right operation!!")