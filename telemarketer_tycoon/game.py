from telemarketer_tycoon import settings
from telemarketer_tycoon.bank import bank
from telemarketer_tycoon.company import Company
from telemarketer_tycoon.event_loop import event_loop
from telemarketer_tycoon.exceptions import GameOver
from telemarketer_tycoon.stats import stat_logger
from telemarketer_tycoon.person import Person


class Game(object):
    def __init__(self):
        self.company = Company()

        dan_the_man = Person('Dan', 0.8)
        dan_the_man.weekly_chance_to_leave = 0
        self.company.add_employee(dan_the_man)
        self.event_loop = event_loop

    def run_week(self):
        self.event_loop.run_for(5)
        self.display_week_info()
        self.pay_wages()
        self.print_total_money()
        self.check_money()
        self.company.check_notice_hand_ins()

    def employee_hiring(self):
        if bank.total < settings.HIRING_COST:
            print(f"You need £{settings.HIRING_COST:,} to hire a new caller!")
            return False
        else:
            bank.subtract_money(settings.HIRING_COST)
            print("You hired a new caller!")
            self.company.hire_employee()
            self.print_callers()
            self.print_total_money()
            return False

    def fire_caller(self, e_num):
        return self.company.fire_employee(e_num)

    def pay_wages(self):
        bank.subtract_money(self.company.wages())

    def print_calls_this_week(self):
        print(f'Calls this week: {stat_logger.calls_in_last_week():,}')

    def print_revenue_this_week(self):
        print(f'Revenue this week: £{stat_logger.revenue_in_last_week():,}')

    def print_total_money(self):
        print(f'Total money: £{bank.total:,}')

    def print_callers(self):
        print(f'You have {self.company.num_employees()} callers')

    def display_week_info(self):
        self.print_callers()
        self.print_calls_this_week()
        self.print_revenue_this_week()

    def check_money(self):
        if bank.total < 0:
            print('You ran out of money!\n\n')
            raise GameOver

    def print_caller_stats(self):
        for e_num, employee in self.company.employees.items():
            daily_wage = settings.CALLER_WEEKLY_WAGE / 5
            daily_profit = stat_logger.avg_revenue(employee) - daily_wage

            print(f'\nCaller: {employee.name} ({e_num})')
            print(f'Calls per day: {stat_logger.avg_calls(employee):,.1f}')
            print(f'Daily turnover: £{stat_logger.avg_revenue(employee):,.2f}')
            print(f'Daily wage: £{daily_wage:,.2f}')
            print(f'Daily profit: £{daily_profit:,.2f}')
            print('\n')
