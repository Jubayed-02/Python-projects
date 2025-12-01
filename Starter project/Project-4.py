# not ready yet

from random import choice 


def run_game():
    word: str = choice(["Jubayed", "Apple", "Mclaren"])

    username: str = input("Please enter your username: ").capitalize()
    print(f"Hello, {username}. Welcome to hangman!")

    #setup
    guessed: str = ""
    tries: int = 3

    while tries > 0:
        blanks: int = 0
        print("\nWord: ", end="")

        for char in word:
            if char in guessed:
                print(char, end="")
            else:
                print("_", end="")
                blanks += 1
        
        print() #adds a blank line
        if not blanks:
            print("You got it!")
            break

        guess: str = input("Enter a letter: ")

        if guess in guessed:
            print("You can't choose same letter simulteniously.")
            print(f"You have already guessed {guess}")
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f"You have only {tries} guesses reamining")
            
            if tries == 0:
                print(f"\nthe word was: {word}")
                break

if __name__ == '__main__':
    run_game()
        
        

            

