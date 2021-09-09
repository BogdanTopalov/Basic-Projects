from Rooms.room import Room


class Apartment(Room):
    def __init__(self):
        super().__init__(max_capacity=5, price_per_night=90)
