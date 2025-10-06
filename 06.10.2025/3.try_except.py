user=int(input("Please add a value:\n"))

try:
    user=int(user)
    print(f"Valoarea introdusa {user} este un numar")
except ValueError:
    print("ai introdus un text nu un numar")
