
while True:
    text = input("Please choose a number between 1 and 3:\n")

    if not text.isdigit():
        print("Invalid option")
        continue

    text = int(text)

    if text == 1:
        print("HI!")
    elif text == 2:
        print("Goodbye!")
    elif text == 3:
        print("Program shutdown!")
        break
    else:
        print("Invalid option")