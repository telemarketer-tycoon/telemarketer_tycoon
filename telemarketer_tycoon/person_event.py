from typing import Callable

from telemarketer_tycoon.event_loop import TimeDependent


class PersonEvent(TimeDependent):
    def __init__(self, expected_duration: int, callback: Callable):
        super().__init__()
        self.expected_duration = expected_duration
        self.callback = callback

    def on_time_step(self):
        if self.event_ended():
            self.callback()

    def event_ended(self) -> bool:
        """Uses `self.expected_duration` to randomly end, or not
        """
        return NotImplemented
