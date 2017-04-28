from telemarketer_tycoon import settings
from telemarketer_tycoon.bank import bank
from telemarketer_tycoon.person import Person
from typing import Dict
from faker import Faker

fake = Faker()

class Company(object):
    def __init__(self):
        self.employees: Dict[int, Person] = {}
        self._employee_number = 0

    def add_employee(self, person):
        self.employees[self.get_next_employee_number()] = person

    def remove_employee(self, e_num):
        e = self.employees.pop(e_num)
        e.stop()

    def hire_employee(self):
        if bank.total < settings.HIRING_COST:
            print(f"You need £{settings.HIRING_COST:,} to hire a new caller!")
        else:
            bank.subtract_money(settings.HIRING_COST)
            name = fake.name()
            print(f"Welcome on board {name}!")
            self.add_employee(Person(name))

    def fire_employee(self, e_num):
        e = self.employees.get(e_num)
        if e is None:
            print(f"Caller #{e_num} doesn't exist")
        elif e.firing_cost() > bank.total:
            print(f"Not enough money to fire {e.name}! You need £{e.firing_cost():,}")
        else:
            print(f"Sorry, {e.name}, you're outta here!")
            bank.subtract_money(e.firing_cost())
            self.remove_employee(e_num)
        return False

    def check_notice_hand_ins(self):
        """Check if any employees have handed in their notice periods."""
        for e_id, e in list(self.employees.items()):  # cant iterate and modify
            if e.wants_to_hand_in_notice():
                self.employees.pop(e_id)
                print(f">>> {e.name}, left to become a teacher.")

    def wages(self):
        return sum(e.wage for e in self.employees.values())

    def num_employees(self):
        return len(self.employees.values())

    def get_next_employee_number(self):
        self._employee_number += 1
        return self._employee_number
