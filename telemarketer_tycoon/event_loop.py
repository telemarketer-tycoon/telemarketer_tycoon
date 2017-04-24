import abc
import time
from typing import List


class TimeDependent(metaclass=abc.ABCMeta):
    def __init__(self):
        event_loop.add_listener(self)

    @abc.abstractmethod
    def on_time_step(self):
        return NotImplemented

    def stop(self):
        event_loop.remove_listener(self)


class EventLoop(object):
    def __init__(self):
        self.listeners: List[TimeDependent] = []
        self.sleep_time = 0.1

    def run(self):
        while True:
            self.run_single_step()

    def run_for(self, time_steps):
        for _ in range(time_steps):
            self.run_single_step()


    def run_single_step(self):
        for listener in self.listeners:
            listener.on_time_step()
        self.sleep()

    def sleep(self):
        time.sleep(self.sleep_time)

    def add_listener(self, listener: TimeDependent):
        self.listeners.append(listener)

    def remove_listener(self, listener: TimeDependent):
        self.listeners.remove(listener)

event_loop = EventLoop()



