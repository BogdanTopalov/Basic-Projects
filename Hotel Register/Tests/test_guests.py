from unittest import TestCase, main
from guest import Guest


class GuestTests(TestCase):
    def setUp(self):
        self.guest = Guest("Test Guest", 25)

    def test_constructor(self):
        self.assertEqual("Test Guest", self.guest.full_name)
        self.assertEqual(25, self.guest.age)

    def test_setter_error_with_zero_age(self):
        with self.assertRaises(ValueError) as ve:
            self.guest.age = 0

        self.assertEqual("Age can not be negative or zero!", str(ve.exception))

    def test_setter_error_with_negative_age(self):
        with self.assertRaises(ValueError) as ve:
            self.guest.age = -5

        self.assertEqual("Age can not be negative or zero!", str(ve.exception))


if __name__ == '__main__':
    main()
