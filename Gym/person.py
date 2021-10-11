class Person:
    def __init__(self, name, age, gender, id_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.id_number = id_number

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError('The person needs to be 16 or older '
                             'to train in the gym!')
        self.__age = value


# TODO add more props
