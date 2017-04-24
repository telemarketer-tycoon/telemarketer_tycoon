from cmd import Cmd

import sys

from telemarketer_tycoon.company import Company
from telemarketer_tycoon.event_loop import event_loop
from telemarketer_tycoon.person import Person
from telemarketer_tycoon.stats import stat_logger


class GamePrompt(Cmd):
    def __init__(self, company):
        super().__init__()
        self.company = company

    def do_continue(self, args):
        """Continue to the next week"""
        return True

    def do_c(self, args):
        """Continue to the next week"""
        return self.do_continue(args)

    def do_hire(self, args):
        """Hire a new caller"""
        print("You hired a new caller!")
        self.company.add_employee(Person())
        return True

    def do_h(self, args):
        """Hire a new caller"""
        return self.do_hire(args)

    def do_quit(self, args):
        """Quit the game"""
        print("GAME OVER")
        return sys.exit(0)

if __name__ == "__main__":
    company = Company()
    company.add_employee(Person())
    prompt = GamePrompt(company)

    for week_no in range(1, 1000):
        print(f'\n\n### WEEK {week_no} ###\n\n')
        event_loop.run_for(7)
        print(f'Total calls made: {stat_logger.total_calls_made():,}.\n'
              f'Total money (before salaries): £{stat_logger.total_money():,}\n')
        after_salary = stat_logger.subtract_money(sum(p.wage for p in company.employees))
        print(f'Total money (after salaries): £{stat_logger.total_money():,}\n')

        if after_salary < 0:
            print('You ran out of money!\n\nGAME OVER\n')
            break

        prompt.cmdloop('What do you want to do?')