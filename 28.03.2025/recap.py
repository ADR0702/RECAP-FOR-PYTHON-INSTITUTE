import random
def game():
    x=random.randint(1,10)
    attempt=0
    max_attempt=3
    while attempt < max_attempt:
        try:
            user=int(input("Please choose a number between 1 and 10:\n"))

            if user > 10 or user < 1:
                print("Respect the reqeust, only numbers between 1 and 10!")
                continue
            attempt+=1
            if user ==x:
                print("You're lucky! You guessed the number!")
                break
            else:
                 print(f"Wrong! {max_attempt - attempt} tries left.")

        except ValueError:
            print("You didn't add a number!!!")
    print(f"Unlucky! the number was {x} ! Game Over!!")
            


game()

    


