from Rooms.room import Room


class EconomyRoom(Room):
    def __init__(self):
        super().__init__(max_capacity=2, price_per_night=30)
