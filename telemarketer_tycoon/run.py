import os
from telemarketer_tycoon.exceptions import GameOver
from telemarketer_tycoon.game import Game
from telemarketer_tycoon.ui import GamePrompt

if __name__ == "__main__":
    game = Game()
    prompt = GamePrompt(game)

    for week_no in range(1, 1000):
        os.system('clear')
        print(f'\n\n### WEEK {week_no} ###\n\n')
        try:
            game.run_week()
            prompt.cmdloop('What do you want to do? (default continue)')
        except GameOver:
            print("#### GAME OVER ####\n")
            break
