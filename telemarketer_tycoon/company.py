from telemarketer_tycoon.person import Person
from faker import Faker

fake = Faker()

class Company(object):
    def __init__(self):
        self.employees = {}
        self._employee_number = 0

    def add_employee(self, person):
        self.employees[self.get_next_employee_number()] = person

    def hire_employee(self):
        name = fake.name()
        self.add_employee(Person(name))

    def fire_employee(self, e_num):
        e = self.employees.pop(e_num, None)
        if e is not None:
            print(f"Sorry, {e.name}, you're outa here!")
            e.stop()
        else:
            print(f"Caller #{e_num} doesnt exist")
        return False

    def check_notice_hand_ins(self):
        """Check if any employees have handed in their notice periods."""
        for e_id in list(self.employees.keys()):  # cant iterate and modify
            e = self.employees[e_id]
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
