class Company(object):
    def __init__(self):
        self.employees = []

    def add_employee(self, person):
        self.employees.append(person)