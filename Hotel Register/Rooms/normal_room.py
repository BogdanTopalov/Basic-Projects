from Rooms.room import Room


class NormalRoom(Room):
    def __init__(self, number):
        super().__init__(number, max_capacity=3, price_per_night=50)
