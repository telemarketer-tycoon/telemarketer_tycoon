from cmd import Cmd

import sys

from telemarketer_tycoon import settings
from telemarketer_tycoon.company import Company
from telemarketer_tycoon.event_loop import event_loop
from telemarketer_tycoon.person import Person
from telemarketer_tycoon.stats import stat_logger


class GamePrompt(Cmd):
    def __init__(self, game):
        super().__init__()
        self.game = game

    def do_continue(self, args):
        """Continue to the next week"""
        return True

    def do_c(self, args):
        """Continue to the next week"""
        return self.do_continue(args)

    def do_hire(self, args):
        """Hire a new caller"""
        return self.game.employee_hiring()

    def do_h(self, args):
        """Hire a new caller"""
        return self.do_hire(args)

    def do_quit(self, args):
        """Quit the game"""
        print("GAME OVER")
        return sys.exit(0)


class Game(object):
    def __init__(self):
        self.company = Company()
        self.company.add_employee(Person())
        self.event_loop = event_loop

    def employee_hiring(self):
        if stat_logger.total_money() < settings.HIRING_COST:
            print(f"You need £{settings.HIRING_COST:,} to hire a new caller!")
            return False
        else:
            stat_logger.subtract_money(settings.HIRING_COST)
            print("You hired a new caller!")
            self.company.add_employee(Person())
            self.print_total_money()
            return True

    def pay_wages(self):
        stat_logger.subtract_money(self.company.wages())

    def print_calls_this_week(self):
        print(f'Calls this week: {stat_logger.calls_in_last_week():,}')

    def print_revenue_this_week(self):
        print(f'Revenue this week: £{stat_logger.revenue_in_last_week():,}')

    def print_total_money(self):
        print(f'Total money: £{stat_logger.total_money():,}')

    def display_week_info(self):
        self.print_calls_this_week()
        self.print_revenue_this_week()


if __name__ == "__main__":
    game = Game()
    prompt = GamePrompt(game)

    for week_no in range(1, 1000):
        print(f'\n\n### WEEK {week_no} ###\n\n')
        game.event_loop.run_for(5)
        game.display_week_info()

        game.pay_wages()
        game.print_total_money()

        if stat_logger.total_money() < 0:
            print('You ran out of money!\n\nGAME OVER\n')
            break

        prompt.cmdloop('What do you want to do?')