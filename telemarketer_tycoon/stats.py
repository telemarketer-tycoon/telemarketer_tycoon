from collections import defaultdict

from telemarketer_tycoon import settings


class StatLogger(object):
    def __init__(self):
        self.caller_calls_per_day = defaultdict(list)
        self.caller_revenue_by_day = defaultdict(list)
        self._total_money = settings.STARTING_MONEY

    def record_calls(self, caller, calls_made):
        self.caller_calls_per_day[caller].append(calls_made)

    def record_money_generated(self, caller, money_made):
        self.caller_revenue_by_day[caller].append(money_made)
        self._total_money += money_made

    def subtract_money(self, amount):
        self._total_money -= amount
        return self._total_money

    def total_money(self):
        return self._total_money

    def total_calls_made(self):
        return sum(call_record for person_record in self.caller_calls_per_day.values()
                                for call_record in person_record)

    def calls_in_last_week(self):
        return sum(
            sum(calls_per_day[-5:]) for calls_per_day in
            self.caller_calls_per_day.values()
        )

    def revenue_in_last_week(self):
        return sum(
            sum(revenue_per_day[-5:]) for revenue_per_day in
            self.caller_revenue_by_day.values()
        )


stat_logger = StatLogger()