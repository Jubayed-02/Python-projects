import random


def RPS():
    # welcome message for the player
    print("Welcome to Rock-Paper-Scissors game!")

    # player and bot point will store here
    bot_point = 0
    player_point = 0

    # valid moves of the game
    valid_moves = ["rock", "paper", "scissors"]  

    # lookup table for now
    winning_con = {"rock": "scissors", "paper": "rock",
                   "scissors": "paper"}  
    while True:
        # user input in lower case !!!
        player_move: str = input("rock/paper/scissors >> ").lower()

        # to exit the game
        if player_move == "exit":
            print("\nThanks for playing the game!\nHave a nice day!")
            break

        # a random move for the bot
        bot_move = random.choice(valid_moves)

        # to check the input is valid or not
        if player_move not in valid_moves:
            print("invalid move!")
            continue

        print("-"*20)  # for styling

        # displaying moves
        print(f"You: {player_move}")  # player's move
        print(f"bot move: {bot_move}")  # bot's move

        # game condition
        if player_move == bot_move:
            print("It's a tie!")
        elif winning_con[player_move] == bot_move:
            print("You won!")
            player_point += 1
        else:
            print("bot won!")
            bot_point += 1

        # score
        print(f"\nPlayer's point: {player_point}")
        print(f"Bot point: {bot_point}")

        # condition to quit the game
        print("** enter 'exit' to quit the game anytime you want! **")
        
        print("-" * 20)  # for styling


if __name__ == "__main__":
    RPS()
