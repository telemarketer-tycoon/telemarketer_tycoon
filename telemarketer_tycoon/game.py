from telemarketer_tycoon import settings
from telemarketer_tycoon.company import Company
from telemarketer_tycoon.event_loop import event_loop
from telemarketer_tycoon.exceptions import GameOver
from telemarketer_tycoon.person import Person
from telemarketer_tycoon.stats import stat_logger


class Game(object):
    def __init__(self):
        self.company = Company()
        self.company.add_employee(Person())
        self.event_loop = event_loop

    def run_week(self):
        self.event_loop.run_for(5)
        self.display_week_info()
        self.pay_wages()
        self.print_total_money()
        self.check_money()

    def employee_hiring(self):
        if stat_logger.total_money() < settings.HIRING_COST:
            print(f"You need £{settings.HIRING_COST:,} to hire a new caller!")
            return False
        else:
            stat_logger.subtract_money(settings.HIRING_COST)
            print("You hired a new caller!")
            self.company.add_employee(Person())
            self.print_callers()
            self.print_total_money()
            return False

    def pay_wages(self):
        stat_logger.subtract_money(self.company.wages())

    def print_calls_this_week(self):
        print(f'Calls this week: {stat_logger.calls_in_last_week():,}')

    def print_revenue_this_week(self):
        print(f'Revenue this week: £{stat_logger.revenue_in_last_week():,}')

    def print_total_money(self):
        print(f'Total money: £{stat_logger.total_money():,}')

    def print_callers(self):
        print(f'You have {self.company.num_employees()} callers')

    def display_week_info(self):
        self.print_callers()
        self.print_calls_this_week()
        self.print_revenue_this_week()

    def check_money(self):
        if stat_logger.total_money() < 0:
            print('You ran out of money!\n\n')
            raise GameOver