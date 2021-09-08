class Room:
    """
    This is the base class for all other rooms
    """
    def __init__(self, number, max_capacity, price_per_night):
        self.number = number
        self.max_capacity = max_capacity
        self.price_per_night = price_per_night
        self.occupied = False
