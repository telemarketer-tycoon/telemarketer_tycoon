class Company(object):
    def __init__(self):
        self.employees = []

    def add_employee(self, person):
        self.employees.append(person)

    def wages(self):
        return sum(e.wage for e in self.employees)

    def num_employees(self):
        return len(self.employees)