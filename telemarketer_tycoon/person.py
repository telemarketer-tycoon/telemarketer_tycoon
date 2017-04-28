import numpy as np

from telemarketer_tycoon import settings
from telemarketer_tycoon.event_loop import TimeDependent
from telemarketer_tycoon.bank import bank
from telemarketer_tycoon.stats import stat_logger
from telemarketer_tycoon import helpers


class Person(TimeDependent):

    def __init__(self,
                 name,
                 call_efficiency=None,
                 charisma=None,
                 chance_to_leave=None):
        super().__init__()
        self.name = name
        self.wage = settings.CALLER_WEEKLY_WAGE
        self.call_efficiency = call_efficiency or np.random.uniform(0.5, 1)
        self.charisma = charisma or np.random.uniform(0.5, 1)
        self.weekly_chance_to_leave = chance_to_leave or np.random.uniform(0.001, 0.002)

    def on_time_step(self):
        calls_made = self.num_calls_made()
        sales_made = int(calls_made * self.success_rate())
        money_made = settings.PRODUCT_VALUE * sales_made
        stat_logger.record_calls(self, calls_made)
        stat_logger.record_sales(self, sales_made)
        stat_logger.record_revenue(self, money_made)
        bank.add_money(money_made)

    def num_calls_made(self):
        return np.random.poisson(self.call_efficiency * 133)

    def success_rate(self):
        return np.random.uniform(0, 0.0333) * self.charisma

    def firing_cost(self):
        return settings.FIRING_WEEKS_WAGES * self.wage

    def wants_to_hand_in_notice(self):
        return helpers.binary_choice(probability_true=self.weekly_chance_to_leave)
