import numpy as np

from telemarketer_tycoon import settings
from telemarketer_tycoon.event_loop import TimeDependent
from telemarketer_tycoon.stats import stat_logger


class Person(TimeDependent):

    def __init__(self):
        super().__init__()
        self.wage = settings.CALLER_WEEKLY_WAGE

    def on_time_step(self):
        num_calls = self.num_calls_made()
        money_made = int(settings.PRODUCT_VALUE * num_calls * self.success_rate())
        stat_logger.record_calls(self, num_calls)
        stat_logger.record_money_generated(self, money_made)

    def num_calls_made(self):
        return np.random.poisson(100)

    def success_rate(self):
        return np.random.uniform(0, 0.025)
