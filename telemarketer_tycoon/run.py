import os
from telemarketer_tycoon.exceptions import GameOver
from telemarketer_tycoon.game import Game
from telemarketer_tycoon.ui import GamePrompt
from telemarketer_tycoon.logo import logo

def play_intro():
    print(f'\n{logo}\n')
    print("\n###\nPress any key to start the game.\n###\n")
    input()

if __name__ == "__main__":
    game = Game()
    prompt = GamePrompt(game)
    play_intro()
    for week_no in range(1, 1000):
        os.system('clear')
        print(f'\n\n### WEEK {week_no} ###\n\n')
        try:
            game.run_week()
            prompt.cmdloop('What do you want to do? (default continue, ? for options)')
        except GameOver:
            print("#### GAME OVER ####\n")
            break
