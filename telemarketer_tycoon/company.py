from telemarketer_tycoon.person import Person


class Company(object):
    def __init__(self):
        self.employees = {}

    def add_employee(self, person):
        assert person.name not in self.employees
        self.employees[person.name] = person

    def hire_employee(self):
        name = f'{self.num_employees() + 1}'
        self.add_employee(Person(name))

    def fire_employee(self, name):
        e = self.employees.pop(name, None)
        e_exists = e is not None
        if e_exists:
            e.stop()
        return e_exists

    def wages(self):
        return sum(e.wage for e in self.employees.values())

    def num_employees(self):
        return len(self.employees.values())