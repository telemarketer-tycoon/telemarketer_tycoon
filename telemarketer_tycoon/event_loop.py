import abc
import time
from typing import List


class EventLoop(object):
    def __init__(self):
        self.listeners: List[TimeDependent] = []
        self.sleep_time = 0.01

    def run(self):
        while True:
            for listener in self.listeners:
                listener.on_time_step()
            self.sleep()

    def sleep(self):
        time.sleep(self.sleep_time)

    def add_listener(self, listener: TimeDependent):
        self.listeners.append(listener)

event_loop = EventLoop()


class TimeDependent(metaclass=abc.ABCMeta):
    def __init__(self):
        event_loop.add_listener(self)

    @abc.abstractmethod
    def on_time_step(self):
        return NotImplemented
