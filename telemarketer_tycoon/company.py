from telemarketer_tycoon.person import Person


class Company(object):
    def __init__(self):
        self.employees = []

    def add_employee(self, person):
        self.employees.append(person)

    def hire_employee(self):
        name = f'{self.num_employees() + 1}'
        self.add_employee(Person(name))

    def wages(self):
        return sum(e.wage for e in self.employees)

    def num_employees(self):
        return len(self.employees)