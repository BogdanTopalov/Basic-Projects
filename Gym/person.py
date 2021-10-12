class Person:
    def __init__(self, name, age, gender, id_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.id_number = id_number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        contain_numbers = any([ch.isdigit() for ch in value])

        if len(value) < 2 and contain_numbers:
            raise ValueError("Person's name must be at least 2 characters "
                             "and can't contain numbers.")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError('The person needs to be 16 or older '
                             'to train in the gym!')
        self.__age = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value.lower() not in ['male', 'female']:
            raise ValueError('Invalid gender! Choose male or female.')
        self.__gender = value


# TODO add more props
