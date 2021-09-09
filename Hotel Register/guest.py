class Guest:
    """
    This class will be initiated when a guest is being registered in the hotel.
    """
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    # Check if the age is valid
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Age can not be negative or zero!")
        self.__age = value
