class Room:
    """
    This is the base class for all other rooms.
    """
    def __init__(self, max_capacity, price_per_night):
        self.max_capacity = max_capacity
        self.price_per_night = price_per_night
        self.occupied = False
        self.cleaned = True
        self.guests_info = []

    def get_guest_info(self):
        info = ["Guests in the room: "]

        for guest in self.guests_info:
            name = guest.full_name
            age = guest.age
            info.append(f"> {name} - {age} years old.")

        return "\n".join(info)
