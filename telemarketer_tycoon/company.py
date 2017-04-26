from telemarketer_tycoon import settings
from telemarketer_tycoon.person import Person
from typing import Dict
from faker import Faker

from telemarketer_tycoon.stats import stat_logger

fake = Faker()

class Company(object):
    def __init__(self):
        self.employees: Dict[int, Person] = {}
        self._employee_number = 0

    def add_employee(self, person):
        self.employees[self.get_next_employee_number()] = person

    def hire_employee(self):
        name = fake.name()
        self.add_employee(Person(name))

    def fire_employee(self, e_num):
        e = self.employees.get(e_num)
        if e is None:
            print(f"Caller #{e_num} doesnt exist")
        elif e.firing_cost() > stat_logger.total_money():
            print(f"Not enough money to fire {e.name}! You need £{e.firing_cost():,}")
        else:
            print(f"Sorry, {e.name}, you're outa here!")
            del self.employees[e_num]
            e.stop()
        return False

    def wages(self):
        return sum(e.wage for e in self.employees.values())

    def num_employees(self):
        return len(self.employees.values())

    def get_next_employee_number(self):
        self._employee_number += 1
        return self._employee_number