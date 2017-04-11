import random

from telemarketer_tycoon.event_loop import TimeDependent
from telemarketer_tycoon.person_event import PersonEvent


class Person(TimeDependent):
    def __init__(self):
        super().__init__()
        self.attributes = PersonAttributes()
        self.current_event: PersonEvent
        self.blocked = False

    def on_time_step(self):
        self.attributes.on_timestep()
        if not self.blocked:
            self.generate_event()

    def on_call_complete(self, duration):
        print(f"Call complete! Lasted: {duration} steps")
        self.blocked = False
        self.current_event = None

    def on_break_complete(self, duration):
        print(f"Break complete! Lasted: {duration} steps")
        self.blocked = False
        self.current_event = None

    def generate_event(self):
        if self.attributes.should_generate_event():
            print("Generated an event!")
            self.current_event = PersonEvent(10, self.on_call_complete)
            self.blocked = True


class PersonAttributes(object):
    def __init__(self):
        super().__init__()

    def on_timestep(self):
        pass

    def event_interval(self):
        return 10

    def should_generate_event(self):
        return random.random() < 1 / self.event_interval()