from collections import defaultdict

from telemarketer_tycoon import settings


class StatLogger(object):
    def __init__(self):
        self.calls_by_caller = defaultdict(int)
        self.money_by_caller = defaultdict(int)
        self._total_money = settings.STARTING_MONEY

    def record_calls(self, caller, calls_made):
        self.calls_by_caller[caller] += calls_made

    def record_money_generated(self, caller, money_made):
        self.money_by_caller[caller] += money_made
        self._total_money += money_made

    def total_money(self):
        return f'£{ self._total_money : ,}'

    def total_calls_made(self):
        return f'{ sum(self.calls_by_caller.values()) : ,}'


stat_logger = StatLogger()