first_number=(input("Please Add first number:\n"))
second_number=(input("Please Add second number:\n"))
operations=["+", "-", "*", "/", "//", "%"]
operation=input("Please choose operation: + , - , * , / , // , %\n")

while not first_number.isnumeric():
    print("You didn't add a number")
    first_number=(input("Please Add first number:\n"))
while not second_number.isnumeric():
    print("You didn't add a number")
    second_number=(input("Please Add second number:\n"))

while operation not in operations:
      print("You didn't choose a valid operation")
      operation=input("Please choose operation: + , - , * , / , // , % \n")

first_number=int(first_number)
second_number=int(second_number)

if operation == "+":
    result=first_number+second_number
    print(f"the sum between {first_number} and {second_number} is {result}")
elif operation == "-":
        result=first_number-second_number
        print(f"the result between {first_number} minus {second_number} is {result}")
elif operation == "*":
        result=first_number*second_number
        print(f"the result between {first_number} and {second_number} is {result}")
elif operation == "/":
        result=first_number/second_number
        print(f"the result between {first_number} and {second_number} is {result}")
elif operation == "//":
        result=first_number//second_number
        print(f"the result between {first_number} and {second_number} is {result}")
elif operation == "%":
        result=first_number%second_number
        print(f"the result between {first_number} and {second_number} is {result}")