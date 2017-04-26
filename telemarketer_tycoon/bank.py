from telemarketer_tycoon import settings


class Bank(object):
    def __init__(self, initial_money):
        self.total = initial_money

    def subtract_money(self, amount):
        self.total -= amount
        return self.total

    def add_money(self, amount):
        self.total += amount
        return self.total

bank = Bank(settings.STARTING_MONEY)