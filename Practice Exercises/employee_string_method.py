class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_string(cls, string):
        params = string.split('-')
        firstname = params[0]
        lastname = params[1]
        salary = int(params[2])
        return cls(firstname, lastname, salary)