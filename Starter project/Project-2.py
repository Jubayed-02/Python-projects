# number guessing game using python

from random import randint

lower_number, higher_number = 1, 10
random_int = randint(lower_number, higher_number)
i: int = 1

print(f"Guess a number between {lower_number} to {higher_number} [3 guesses]")

while True:
    if i == 4:
        break

    try:
        user_input: int = int(input(f"\nGuess[no-{i}]: "))

    except ValueError as e:
        print("Please enter a valid input")
        i += 1
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
    i += 1

print(f"The answer: {random_int}")
