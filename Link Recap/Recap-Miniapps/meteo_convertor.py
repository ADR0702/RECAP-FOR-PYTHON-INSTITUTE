# What you need to do:
# Ask the user for the temperature and the unit (C or F).
# Convert F → C or C → F.
# Use:
# functions
# if statements
# numeric input vs string input

def temperature_converter():
    while True:
        user=input("Please choose the measurement unit: Celsius Or Fahrenheit\n").lower()
        if user == "celsius":
            while True:
                temperature=(input("Please type the temperature:\n"))
                try:
                    temperature=float(temperature)
                    break
                except ValueError:
                    print("Wrong Please type a valid number")
            fahrenheit=temperature * 1.8 +32
            print(f"The fahrenheit temperature outside is {fahrenheit}")
            break
        elif user == "fahrenheit":
            while True:
                temperature=(input("Please type the temperature:\n"))
                try:
                    temperature=float(temperature)
                    break
                except ValueError:
                    print("Wrong Please type a valid number")
            celsius=(temperature-32) / 1.8
            print(f"The celsius temperature outside is {celsius}")
            break
        else:
            user=input("The chosen measurement doesn't exist! Please choose the measurement unit: Celsius Or Fahrenheit\n").lower()

    
temperature_converter()