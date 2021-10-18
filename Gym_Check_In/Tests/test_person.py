from unittest import TestCase, main
from Gym_Check_In.person import Person


class PersonTests(TestCase):
    def setUp(self):
        self.person = Person('Bogdan', 22, 'male', True)

    def test_constructor(self):
        self.assertEqual('Bogdan', self.person.name)
        self.assertEqual(22, self.person.age)
        self.assertEqual('male', self.person.gender)
        self.assertEqual(True, self.person.has_clean_shoes)
        self.assertEqual(False, self.person.membership)

    def test_name_property_with_too_short_name(self):
        expected_result = "Person's name must be at least 2 characters long."

        with self.assertRaises(ValueError) as ve:
            self.person.name = 'A'

        self.assertEqual(expected_result, str(ve.exception))

    def test_name_property_with_empty_string(self):
        expected_result = "Person's name must be at least 2 characters long."

        with self.assertRaises(ValueError) as ve:
            self.person.name = ''

        self.assertEqual(expected_result, str(ve.exception))

    def test_name_property_working_as_intended(self):
        self.person.name = 'Test Name'
        self.assertEqual('Test Name', self.person.name)

    def test_age_property_with_string(self):
        with self.assertRaises(ValueError) as ve:
            self.person.age = '20'

        self.assertEqual('Age must be a number!', str(ve.exception))

    def test_age_property_with_boolean(self):
        with self.assertRaises(ValueError) as ve:
            self.person.age = True

        self.assertEqual('Age must be a number!', str(ve.exception))

    def test_age_property_when_age_is_too_low(self):
        expected_result = 'The person has to be 16 or older ' \
                          'to train in the gym!'

        with self.assertRaises(ValueError) as ve:
            self.person.age = 10

        self.assertEqual(expected_result, str(ve.exception))


if __name__ == '__main__':
    main()
