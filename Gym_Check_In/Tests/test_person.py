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

    def test_name_property_getter_and_setter(self):
        pass


if __name__ == '__main__':
    main()
