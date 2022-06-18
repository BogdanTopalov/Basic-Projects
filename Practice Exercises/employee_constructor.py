class Employee:
    def __init__(self, full_name, salary=None, height=None, nationality=None, subordinates=None):
        self.full_name = full_name
        self.name = full_name.split()[0]
        self.lastname = full_name.split()[1]
        self.salary = salary
        self.height = height
        self.nationality = nationality
        self.subordinates = subordinates
