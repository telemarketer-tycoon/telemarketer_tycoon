import numpy as np

from telemarketer_tycoon import settings
from telemarketer_tycoon.event_loop import TimeDependent
from telemarketer_tycoon.stats import stat_logger


class Person(TimeDependent):

    def __init__(self, name, call_efficiency=None):
        super().__init__()
        self.name = name
        self.wage = settings.CALLER_WEEKLY_WAGE
        self.call_efficiency = call_efficiency or np.random.uniform(0.5, 1)

    def on_time_step(self):
        num_calls = self.num_calls_made()
        money_made = settings.PRODUCT_VALUE * int(num_calls * self.success_rate())
        stat_logger.record_calls(self, num_calls)
        stat_logger.record_money_generated(self, money_made)

    def num_calls_made(self):
        return np.random.poisson(self.call_efficiency * 133)

    def success_rate(self):
        return np.random.uniform(0, 0.025)

    def firing_cost(self):
        return settings.FIRING_WEEKS_WAGES * self.wage
