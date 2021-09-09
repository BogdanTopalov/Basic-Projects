from Rooms.room import Room


class NormalRoom(Room):
    def __init__(self):
        super().__init__(max_capacity=3, price_per_night=50)
