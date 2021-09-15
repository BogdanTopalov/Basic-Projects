from unittest import TestCase, main
from Rooms.room import Room
from Rooms.economy_room import EconomyRoom
from Rooms.normal_room import NormalRoom
from Rooms.apartment import Apartment
from guest import Guest


class RoomTests(TestCase):
    def setUp(self) -> None:
        self.room = Room(5, 90)

    def test_constructor(self):
        self.assertEqual(5, self.room.max_capacity)
        self.assertEqual(90, self.room.price_per_night)
        self.assertEqual(False, self.room.occupied)
        self.assertEqual(True, self.room.cleaned)
        self.assertEqual([], self.room.guests_info)

    def test_get_guest_info_method_when_guests_info_list_is_empty(self):
        expected_result = "There are no guests in the room."
        result = self.room.get_guest_info()
        self.assertEqual(expected_result, result)

    def test_get_guest_info_method_with_guests_in_the_room(self):
        guest1 = Guest("Bogdan Topalov", 22)
        guest2 = Guest("Test Person", 25)
        guest3 = Guest("John Wick", 55)

        self.room.guests_info = [guest1, guest2, guest3]

        expected_result = "Guests in the room: \n" \
                          "> Bogdan Topalov - 22 years old.\n" \
                          "> Test Person - 25 years old.\n" \
                          "> John Wick - 55 years old."
        result = self.room.get_guest_info()

        self.assertEqual(expected_result, result)

    def test_economy_room_constructor(self):
        economy_room = EconomyRoom()
        self.assertEqual(2, economy_room.max_capacity)
        self.assertEqual(30, economy_room.price_per_night)
        self.assertEqual(False, economy_room.occupied)
        self.assertEqual(True, economy_room.cleaned)
        self.assertEqual([], economy_room.guests_info)

    def test_normal_room_constructor(self):
        normal_room = NormalRoom()
        self.assertEqual(3, normal_room.max_capacity)
        self.assertEqual(50, normal_room.price_per_night)
        self.assertEqual(False, normal_room.occupied)
        self.assertEqual(True, normal_room.cleaned)
        self.assertEqual([], normal_room.guests_info)

    def test_apartment_constructor(self):
        apartment = Apartment()
        self.assertEqual(5, apartment.max_capacity)
        self.assertEqual(90, apartment.price_per_night)
        self.assertEqual(False, apartment.occupied)
        self.assertEqual(True, apartment.cleaned)
        self.assertEqual([], apartment.guests_info)


if __name__ == '__main__':
    main()
