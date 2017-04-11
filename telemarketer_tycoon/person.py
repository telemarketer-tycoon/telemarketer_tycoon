import random
from collections import namedtuple
from typing import List

from telemarketer_tycoon.event_loop import TimeDependent
from telemarketer_tycoon.person_event import PersonEvent

Call = namedtuple('Call', ['duration'])

class PersonStats(object):
    def __init__(self):
        self.calls_made: List[Call] = []

    def record_call(self, duration):
        self.calls_made.append(Call(duration))

    def total_call_duration(self):
        return sum(c.duration for c in self.calls_made)

    def total_calls(self):
        return len(self.calls_made)

    def average_time_per_call(self):
        return self.total_call_duration() / self.total_calls()


class Person(TimeDependent):
    def __init__(self):
        super().__init__()
        self.attributes = PersonAttributes()
        self.stats = PersonStats()
        self.current_event: PersonEvent
        self.blocked = False

    def on_time_step(self):
        self.attributes.on_timestep()
        if not self.blocked:
            self.generate_event()

    def on_call_complete(self, duration):
        print(f"Call complete! Lasted: {duration} minutes")
        self.blocked = False
        self.current_event = None
        self.stats.record_call(duration)

    def generate_event(self):
        if self.attributes.should_generate_call_event():
            print("Generated an event!")
            self.current_event = PersonEvent(5, self.on_call_complete)
            self.blocked = True


class PersonAttributes(object):
    def __init__(self):
        self.energy = 100
        self.efficiency = 50
        self.morale = 75

    def on_timestep(self):
        self.energy -= 0.05

    def call_event_interval(self):
        dials_a_day = 20 + 180 * (self.efficiency / 100 +
                                  self.energy / 100 +
                                  self.morale / 100)
        return 8 * 60 / dials_a_day

    def should_generate_call_event(self):
        return random.random() < 1 / self.call_event_interval()