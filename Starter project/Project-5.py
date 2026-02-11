import random, sys


class RPS:
    def __init__(self):
        
        print("Welcome to Rock-Paper-Scissors game!")

        self.moves: dict = {"rock":"👊🏻", "paper": "📜", "scissors":"✂️"}
        self.valid_moves: list[str] = list(self.moves.keys())


    def play_game(self):
        
        user_move: str = input("rock/paper/scissors >> ").lower()

        if user_move == "exit":
            print("*"*20)
            print("Thanks for playing the game!")
            sys.exit()

        if user_move not in self.valid_moves:
            print("Invalid move!")
            return self.play_game()
        
        bot_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, bot_move)
        self.check_moves(user_move, bot_move)


    def display_moves(self, user_move: str, bot_move: str):
        print("-"*20)
        print(f"You: {self.moves[user_move]}")
        print(f"Bot: {self.moves[bot_move]}")
        print("-"*20)

    def check_moves(self, user_move: str, bot_move: str):
        if user_move == bot_move:
            print('It\'s a tie!')
        elif user_move == "rock" and bot_move == "scissors":
            print("You won!")
        elif user_move == "paper" and bot_move == "rock":
            print("You won!")
        elif user_move == "scissor" and bot_move == "paper":
            print("You won!")
        else:
            print("Bot won!")

if __name__ == "__main__":
    rps = RPS()
    while True:
        rps.play_game()
