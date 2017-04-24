from telemarketer_tycoon.company import Company
from telemarketer_tycoon.event_loop import event_loop
from telemarketer_tycoon.person import Person
from telemarketer_tycoon.stats import stat_logger

if __name__ == "__main__":
    company = Company()
    company.add_employee(Person())

    game_over = False
    while not game_over:
        event_loop.run_for(7)
        print(f'Total calls made: {stat_logger.total_calls_made():,}.\n'
              f'Total money (before salaries): £{stat_logger.total_money():,}\n')
        after_salary = stat_logger.subtract_money(sum(p.wage for p in company.employees))
        print(f'Total money (after salaries): £{stat_logger.total_money():,}\n')
        if after_salary < 0:
            print('You ran out of money!\n\nGAME OVER\n')
            game_over = True