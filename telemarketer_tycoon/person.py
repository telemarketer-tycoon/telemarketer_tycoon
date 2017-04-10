from telemarketer_tycoon.event_loop import TimeDependent


class Person(TimeDependent):
    def __init__(self):
        super().__init__()
        self.attributes = PersonAttributes()

    def on_time_step(self):
        self.attributes.on_timestep()

    def on_event_complete(self, duration):
        pass


class PersonAttributes(object):
    def __init__(self):
        super().__init__()

    def on_timestep(self):
        pass