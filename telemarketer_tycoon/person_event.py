from typing import Callable

from telemarketer_tycoon.event_loop import TimeDependent
from telemarketer_tycoon.person import Person


class PersonEvent(TimeDependent):
    def __init__(self, expected_duration: int, callback: Callable):
        super().__init__()
        self.expected_duration = expected_duration
        self.callback = callback
        self.duration = 0

    def on_time_step(self):
        self.duration += 1
        if self.event_ended():
            self.callback(self.duration)

    def event_ended(self) -> bool:
        """Uses `self.expected_duration` to randomly end, or not
        """
        return NotImplemented


def generate_call_event(person: Person):
    return PersonEvent(5, person.on_event_complete)

def generate_break_event(person: Person):
    return PersonEvent(20, person.on_event_complete)