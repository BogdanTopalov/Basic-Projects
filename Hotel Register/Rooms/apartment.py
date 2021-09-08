from Rooms.room import Room


class Apartment(Room):
    def __init__(self, number):
        super().__init__(number, max_capacity=5, price_per_night=90)
