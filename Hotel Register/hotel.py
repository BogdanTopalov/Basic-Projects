from Rooms.economy_room import EconomyRoom
from Rooms.normal_room import NormalRoom
from Rooms.apartment import Apartment


possible_rooms = {
    "economy": EconomyRoom,
    "normal": NormalRoom,
    "apartment": Apartment
}


class Hotel:
    """
    This is the main class.
    """
    def __init__(self, name, rooms_capacity):
        self.name = name
        self.rooms_capacity = rooms_capacity
        # Store room numbers and room's class object as key:value pair.
        self.rooms = {}

    def add_room(self, room_type):

        # Check if the hotel reached its maximum room capacity.
        if self.rooms_capacity <= len(self.rooms):
            return f"Hotel reached it's maximum room capacity. " \
                   f"No more rooms can be added!"

        # Check if room_type is valid.
        if room_type.lower() not in possible_rooms:
            return f"{self.name} doesn't offer {room_type} rooms."

        # Initialize room class and add it to the hotel rooms.
        room_number = len(self.rooms) + 1
        room = possible_rooms[room_type]
        self.rooms[room_number] = room

    # Guests arguments are received as class objects.
    def register_guests(self, wanted_room, stay_in_nights, *guests):

        # Check if the wanted room is valid.
        if wanted_room.lower() not in possible_rooms:
            return f"{self.name} doesn't offer {wanted_room} rooms."

        # Check if the wanted room is available.
        available_rooms = [
            n
            for n, room in self.rooms.items()
            if type(room).__name__ == wanted_room.lower()
        ]
        if not available_rooms:
            return f"There are no {wanted_room} rooms available."

        # Take the first available room.
        room_number = available_rooms[0]

        # Check if there is enough room space for the guests.
        room_capacity = self.rooms[room_number].max_capacity
        if len(guests) > room_capacity:
            return f"Too many guests! Room's maximum capacity is {room_capacity}."

        # Add guests into the room's info list.
        for g in guests:
            self.rooms[room_number].guests_info.append(g)

        # Change the two boolean attributes.
        self.rooms[room_number].occupied = True
        self.rooms[room_number].cleaned = False

        # Calculate the room price for the stay period.
        total_stay_price = self.rooms[room_number].price_per_night * stay_in_nights

        return f"Guests are successfully registered in room №{room_number}. " \
               f"The price for their stay is {total_stay_price:.2f}."

    def free_room(self, room_number):

        # Check if the room is occupied.
        if not self.rooms[room_number].occupied:
            return f"Room №{room_number} is already free."

        # Free and clean the room.
        self.rooms[room_number].guests_info = []
        self.rooms[room_number].occupied = False
        self.rooms[room_number].cleaned = True

        return f"Room №{room_number} is now available for reservation."
