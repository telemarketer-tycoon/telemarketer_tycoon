from telemarketer_tycoon.event_loop import event_loop
from telemarketer_tycoon.person import Person

if __name__ == "__main__":
    person = Person()
    event_loop.run_for(480)
    print(f'Total calls made {person.stats.total_calls()}.\n'
          f'Total duration {person.stats.total_call_duration()} minutes\n'
          f'Average call duration {person.stats.average_time_per_call()}')