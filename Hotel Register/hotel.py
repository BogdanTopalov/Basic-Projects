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

    @staticmethod
    def get_occupied_rooms(rooms):
        occupied_rooms = [r for r in rooms.values() if r.occupied]
        return occupied_rooms

    @staticmethod
    def get_total_guests(rooms):
        total_guests = sum([
            len(r.guests_info)
            for r in rooms.values()
            if r.guests_info
        ])
        return total_guests

    def add_room(self, room_type):

        # Check if the hotel reached its maximum room capacity.
        if self.rooms_capacity <= len(self.rooms):
            return "Hotel reached it's maximum room capacity. " \
                   "No more rooms can be added!"

        # Check if room_type is valid.
        if room_type.lower() not in possible_rooms:
            return f"{self.name} doesn't offer {room_type} rooms."

        # Initialize room class and add it to the hotel rooms.
        room_number = len(self.rooms) + 1
        room = possible_rooms[room_type.lower()]
        self.rooms[room_number] = room

        return f"{room_type} room has been added to the hotel."

    # Guests arguments are received as class objects.
    def register_guests(self, wanted_room, stay_in_nights, *guests):

        # Check if the wanted room is valid.
        if wanted_room.lower() not in possible_rooms:
            return f"{self.name} doesn't offer {wanted_room} rooms."

        # Check if the wanted room is available
        # and there is enough space for the guests.
        available_rooms = [
            n
            for n, room in self.rooms.items()
            if type(room).__name__.lower() == wanted_room.lower()+"room"
            and room.max_capacity >= len(guests)
            and not room.occupied
        ]
        if not available_rooms:
            return f"There are no {wanted_room} rooms available."

        # Take the first available room.
        room_number = available_rooms[0]

        # Add guests into the room's info list.
        for g in guests:
            self.rooms[room_number].guests_info.append(g)

        # Change the two boolean attributes.
        self.rooms[room_number].occupied = True
        self.rooms[room_number].cleaned = False

        # Calculate the room price for the stay period.
        total_stay_price = self.rooms[room_number].price_per_night * stay_in_nights

        return f"Guests are successfully registered in room ???{room_number}. " \
               f"The price for their stay is {total_stay_price:.2f}."

    def free_room(self, room_number):

        # Check if the room is occupied.
        if not self.rooms[room_number].occupied:
            return f"Room ???{room_number} is already free."

        # Free and clean the room.
        self.rooms[room_number].guests_info = []
        self.rooms[room_number].occupied = False
        self.rooms[room_number].cleaned = True

        return f"Room ???{room_number} is now available for reservation."

    def get_room_info(self, room_number):

        # Check if room number is valid.
        if room_number not in self.rooms:
            return f"No room ???{room_number} in the hotel."

        room_info = [f"Room ???{room_number}:"]

        room = self.rooms[room_number]

        room_info.append(f"Type - {type(room).__name__}")
        room_info.append(f"Max capacity - {room.max_capacity}")
        room_info.append(f"Price per night - {room.price_per_night}")

        # Assign correct room boolean attributes.
        occupied = "Occupied" if room.occupied else "Free"
        cleaned = "Cleaned" if room.cleaned else "Not cleaned"

        room_info.append(f"Status - {occupied} and {cleaned}")

        # Check if "get_guest_info" method should be called.
        if room.occupied:
            room_info.append(room.get_guest_info())

        return "\n".join(room_info)

    def info(self):
        hotel_info = []

        # Calculate how many rooms are occupied.
        total_occupied_rooms = len(Hotel.get_occupied_rooms(self.rooms))

        # Calculate how many guests are currently in the hotel.
        total_guests = Hotel.get_total_guests(self.rooms)

        hotel_info.append(f"Hotel {self.name}")
        hotel_info.append(f"Occupied rooms: {total_occupied_rooms}")
        hotel_info.append(f"Total guests in the hotel: {total_guests}")

        return "\n".join(hotel_info)
