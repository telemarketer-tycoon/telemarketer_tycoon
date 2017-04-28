import abc
import random

from telemarketer_tycoon import helpers


class Event(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.previously_triggered = False
        self.stage = 0

    @abc.abstractmethod
    def triggered(self, company):
        pass

    @abc.abstractmethod
    def action(self, company):
        pass


class TeacherRecruitingDrive(Event):
    trigger_chance = 0.01

    def triggered(self, company):
        num_employees = len(company.employees)
        if not self.previously_triggered and num_employees >= 10:
            return helpers.binary_choice(probability_true=self.trigger_chance)
        return False

    def action(self, company):
        num_leavers = int(len(company.employees) / 2)
        print(f"The local school upped their recruiting efforts, {num_leavers} employees quit.")

        for _ in range(num_leavers):
            e_id, e = random.choice(list(company.employees.items()))
            company.remove_employee(e_id)
            print(f" - {e.name} is outta here!")