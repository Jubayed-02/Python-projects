# number guessing game using python

from random import randint

# greetings section
print("Welcome to 'Number Guessing Game' made by Shadow!\n")
username: str = input("Enter your username: ").capitalize()
print(f"Hi, {username}. Let's play the game!\n")

# main code
lower_number, higher_number = 1, 10
random_int = randint(lower_number, higher_number)


print(f"Guess a number between {lower_number} to {higher_number} [3 guesses]")

for i in range(3, 0, -1):
    try:
        user_input: int = int(input(f"\nGuess[no-{i}]: "))

    except ValueError as e:
        print("Please enter a valid input")
        continue

    if user_input > higher_number or user_input < lower_number:
        print("please follow the instruction! don't do anything silly")
    elif user_input < random_int:
        print("The number is higher than you thought!")
    elif user_input > random_int:
        print("The number is lower than you thought!")
    else:
        print("You guessed it!")
        break

print(f"The answer: {random_int}")

