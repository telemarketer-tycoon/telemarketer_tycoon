from telemarketer_tycoon.exceptions import GameOver
from telemarketer_tycoon.game import Game
from telemarketer_tycoon.stats import stat_logger
from telemarketer_tycoon.ui import GamePrompt

if __name__ == "__main__":
    game = Game()
    prompt = GamePrompt(game)

    for week_no in range(1, 1000):
        print(f'\n\n### WEEK {week_no} ###\n\n')
        try:
            game.event_loop.run_for(5)
            game.display_week_info()

            game.pay_wages()
            game.print_total_money()
            game.check_money()

            prompt.cmdloop('What do you want to do? (default continue)')
        except GameOver:
            print("#### GAME OVER ####\n")
            break