from unittest import TestCase, main
from hotel import Hotel, possible_rooms
from Rooms.economy_room import EconomyRoom
from Rooms.normal_room import NormalRoom
from Rooms.apartment import Apartment
from guest import Guest


class HotelTests(TestCase):
    def setUp(self):
        self.hotel = Hotel("Test Plaza", 5)
        self.eco_room = EconomyRoom()
        self.normal_room = NormalRoom()
        self.apartment = Apartment()
        self.guest1 = Guest("Test Person", 25)
        self.guest2 = Guest("Bogdan Topalov", 22)

    def test_constructor(self):
        self.assertEqual("Test Plaza", self.hotel.name)
        self.assertEqual(5, self.hotel.rooms_capacity)
        self.assertEqual({}, self.hotel.rooms)

    def test_possible_rooms_mapper(self):
        self.assertEqual(EconomyRoom, possible_rooms["economy"])
        self.assertEqual(NormalRoom, possible_rooms["normal"])
        self.assertEqual(Apartment, possible_rooms["apartment"])

    def test_staticmethod_get_occupied_rooms(self):
        self.eco_room.occupied = True

        self.hotel.rooms = {1: self.eco_room, 2: self.normal_room, 3: self.apartment}

        expected_result = [self.eco_room]
        result = self.hotel.get_occupied_rooms(self.hotel.rooms)
        self.assertEqual(expected_result, result)

    def test_staticmethod_get_total_guests(self):
        self.eco_room.guests_info = [self.guest1, self.guest2]
        self.hotel.rooms = {1: self.eco_room}

        expected_result = 2
        result = self.hotel.get_total_guests(self.hotel.rooms)
        self.assertEqual(expected_result, result)

    def test_add_room_method_when_maximum_rooms_capacity_is_reached(self):
        self.hotel.rooms_capacity = 3
        self.hotel.rooms = {1: self.eco_room, 2: self.normal_room, 3: self.apartment}

        expected_result = "Hotel reached it's maximum room capacity. " \
                          "No more rooms can be added!"
        result = self.hotel.add_room("economy")
        self.assertEqual(expected_result, result)

    def test_add_room_method_when_invalid_room_type_is_given(self):
        expected_result = "Test Plaza doesn't offer luxury rooms."
        result = self.hotel.add_room("luxury")
        self.assertEqual(expected_result, result)

    def test_add_room_method_working_properly(self):
        expected_result = "Normal room has been added to the hotel."
        result = self.hotel.add_room("Normal")
        self.assertEqual(expected_result, result)
        self.assertEqual({1: NormalRoom}, self.hotel.rooms)

    def test_register_guests_method_when_invalid_wanted_room_is_given(self):
        expected_result = "Test Plaza doesn't offer president rooms."
        result = self.hotel.register_guests("president", 5, self.guest1)
        self.assertEqual(expected_result, result)

    def test_register_guests_method_with_no_available_rooms_due_to_occupation(self):
        self.eco_room.occupied = True
        self.hotel.rooms = {1: self.eco_room}

        expected_result = "There are no economy rooms available."
        result = self.hotel.register_guests("economy", 5, self.guest2)
        self.assertEqual(expected_result, result)

    def test_register_guests_method_with_no_available_rooms_due_to_capacity_problem(self):
        self.eco_room.max_capacity = 1
        self.hotel.rooms = {1: self.eco_room}

        expected_result = "There are no economy rooms available."
        result = self.hotel.register_guests("economy", 5, self.guest1, self.guest2)
        self.assertEqual(expected_result, result)

    def test_register_guests_method_working_properly(self):
        self.hotel.rooms = {1: self.eco_room}

        expected_result = "Guests are successfully registered in room №1. " \
                          "The price for their stay is 90.00."
        result = self.hotel.register_guests("economy", 3, self.guest1, self.guest2)
        self.assertEqual(expected_result, result)
        self.assertEqual(True, self.hotel.rooms[1].occupied)
        self.assertEqual(False, self.hotel.rooms[1].cleaned)
        self.assertEqual([self.guest1, self.guest2], self.hotel.rooms[1].guests_info)

    def test_free_room_method_when_room_is_not_occupied(self):
        self.hotel.rooms = {1: self.eco_room}

        expected_result = "Room №1 is already free."
        result = self.hotel.free_room(1)
        self.assertEqual(expected_result, result)

    def test_free_room_method_working_properly(self):
        self.eco_room.occupied = True
        self.eco_room.cleaned = False
        self.eco_room.guests_info = [self.guest1]

        self.hotel.rooms = {1: self.eco_room}

        expected_result = "Room №1 is now available for reservation."
        result = self.hotel.free_room(1)
        self.assertEqual(expected_result, result)
        self.assertEqual(False, self.hotel.rooms[1].occupied)
        self.assertEqual(True, self.hotel.rooms[1].cleaned)
        self.assertEqual([], self.hotel.rooms[1].guests_info)

    def test_get_room_info_method_when_number_is_invalid(self):
        self.hotel.rooms = {1: self.apartment}

        expected_result = "No room №3 in the hotel."
        result = self.hotel.get_room_info(3)
        self.assertEqual(expected_result, result)

    def test_get_room_info_method_working_properly_when_room_is_occupied(self):
        self.eco_room.occupied = True
        self.eco_room.cleaned = False
        self.eco_room.guests_info = [self.guest1, self.guest2]

        self.hotel.rooms = {1: self.eco_room}

        expected_result = "Room №1:\n" \
                          "Type - EconomyRoom\n" \
                          "Max capacity - 2\n" \
                          "Price per night - 30\n" \
                          "Status - Occupied and Not cleaned\n" \
                          "Guests in the room: \n" \
                          "> Test Person - 25 years old.\n" \
                          "> Bogdan Topalov - 22 years old."
        result = self.hotel.get_room_info(1)
        self.assertEqual(expected_result, result)

    def test_get_room_info_method_working_properly_when_room_is_free(self):
        self.hotel.rooms = {1: self.apartment}

        expected_result = "Room №1:\n" \
                          "Type - Apartment\n" \
                          "Max capacity - 5\n" \
                          "Price per night - 90\n" \
                          "Status - Free and Cleaned"
        result = self.hotel.get_room_info(1)
        self.assertEqual(expected_result, result)

    def test_info_method_working_properly(self):
        self.eco_room.occupied = True
        self.eco_room.guests_info = [self.guest1]
        self.normal_room.occupied = True
        self.normal_room.guests_info = [self.guest2]

        self.hotel.rooms = {1: self.eco_room, 2: self.normal_room, 3: self.apartment}

        expected_result = "Hotel Test Plaza\n" \
                          "Occupied rooms: 2\n" \
                          "Total guests in the hotel: 2"
        result = self.hotel.info()
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
