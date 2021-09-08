from Rooms.room import Room


class EconomyRoom(Room):
    def __init__(self, number):
        super().__init__(number, max_capacity=2, price_per_night=30)
