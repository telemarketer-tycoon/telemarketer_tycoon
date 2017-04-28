from collections import defaultdict

import numpy as np

from telemarketer_tycoon import ui


class StatLogger(object):
    def __init__(self):
        self.caller_calls_per_day = defaultdict(list)
        self.caller_revenue_per_day = defaultdict(list)
        self.caller_sales_per_day = defaultdict(list)

    def record_calls(self, caller, calls_made):
        self.caller_calls_per_day[caller].append(calls_made)

    def record_revenue(self, caller, money_made):
        self.caller_revenue_per_day[caller].append(money_made)

    def record_sales(self, caller, sales_made):
        self.caller_sales_per_day[caller].append(sales_made)

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
            self.caller_revenue_per_day.values()
        )

    def avg_calls(self, employee) -> float:
        calls = self.caller_calls_per_day[employee] or [0]
        return np.mean(calls)

    def avg_last_week(self, records, employee):
        all_records = records[employee]
        if all_records:
            return np.mean(all_records[-5:])
        else:
            return 0

    def avg_revenue(self, employee) -> float:
        revenues = self.caller_revenue_per_day[employee] or [0]
        return np.mean(revenues)

    def avg_sales(self, employee) -> float:
        sales = self.caller_sales_per_day[employee] or [0]
        return np.mean(sales)

    def daily_profit(self, employee):
        daily_wage = employee.wage / 5
        return self.avg_revenue(employee) - daily_wage

    def stats_table(self, employee):
        return [
            ['Stat', 'Daily Average', 'Last week'],
            ['Calls', ui.format_float(self.avg_calls(employee)), ui.format_float(self.avg_last_week(self.caller_calls_per_day, employee))],
            ['Sales', ui.format_float(self.avg_sales(employee)), ui.format_float(self.avg_last_week(self.caller_sales_per_day, employee))],
            ['Revenue', ui.format_money(self.avg_revenue(employee)), ui.format_float(self.avg_last_week(self.caller_revenue_per_day, employee))],
            ['Profit', ui.format_money(self.daily_profit(employee)), '']
        ]

stat_logger = StatLogger()