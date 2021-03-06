class Person:
    def __init__(self, name, age, gender, has_clean_shoes):
        self.name = name
        self.age = age
        self.gender = gender
        self.has_clean_shoes = has_clean_shoes
        self.membership = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Person's name must be at least 2 characters long.")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if type(value) != int:
            raise ValueError('Age must be a number!')

        if value < 16:
            raise ValueError('The person has to be 16 or older '
                             'to train in the gym!')
        self.__age = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if type(value) != str:
            raise ValueError('Gender value must be sting.')

        value = value.lower()

        if value not in ['male', 'female']:
            raise ValueError("Person's gender has to be either male or female.")
        self.__gender = value

    @property
    def has_clean_shoes(self):
        return self.__has_clean_shoes

    @has_clean_shoes.setter
    def has_clean_shoes(self, value):
        if type(value) != bool:
            raise ValueError('has_clean_shoes property can be either True or False.')
        self.__has_clean_shoes = value

    @property
    def membership(self):
        return self.__membership

    @membership.setter
    def membership(self, value):
        if type(value) != bool:
            raise ValueError('Membership property must be boolean.')
        self.__membership = value
