from telemarketer_tycoon.event_loop import event_loop
from telemarketer_tycoon.person import Person
from telemarketer_tycoon.stats import stat_logger

if __name__ == "__main__":
    person = Person()
    event_loop.run_for(7)
    print(f'Total calls made: {stat_logger.total_calls_made()}.\n'
          f'Total money (before salaries): {stat_logger.total_money()}\n')