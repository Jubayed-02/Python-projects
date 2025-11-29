# dice simulator using a python program
import random

def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for i in range(amount):
        rolling_number: int = random.randint(1, 6)
        rolls.append(rolling_number)
    return rolls

def main():
    while True:       
        try:
            print("How many dice would you like to roll? \n[Press 'exit' to leave]")
            
            user_input = input(": ").lower()
            if user_input == "exit":
                print("Thanks for playing!")
                break

            result = roll_dice(int(user_input))
            print(*result, sep=", ")
            print(f"Total: {sum(result)}\n")

        except ValueError:
            print("Enter a valid number!")

if __name__== '__main__':
    main()