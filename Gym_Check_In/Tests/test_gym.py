from unittest import TestCase, main
from Gym_Check_In.gym import Gym
from Gym_Check_In.person import Person


class GymTests(TestCase):
    def setUp(self):
        self.gym = Gym('Muscle Power', 100)
        self.person = Person('Bogdan', 23, 'male', True)

    def test_constructor(self):
        self.assertEqual('Muscle Power', self.gym.gym_name)
        self.assertEqual(100, self.gym.max_capacity)
        self.assertEqual([], self.gym.currently_in)

    def test_check_in_method_when_gym_is_full(self):
        self.gym.max_capacity = 1
        self.gym.currently_in = [self.person]

        expected_result = "Muscle Power Gym is full at the moment. " \
                          "Try checking in later."
        self.assertEqual(expected_result, self.gym.check_in(self.person))

    def test_check_in_method_when_person_does_not_have_active_membership(self):
        self.person.membership = False

        expected_result = "Bogdan's membership is not active. " \
                          "Please activate it before checking in."
        self.assertEqual(expected_result, self.gym.check_in(self.person))

    def test_check_in_method_when_person_does_not_have_clean_shoes(self):
        self.person.membership = True
        self.person.has_clean_shoes = False

        expected_result = "Bogdan doesn't have clean shoes. " \
                          "In order to be checked in, Bogdan must have clean shoes."
        self.assertEqual(expected_result, self.gym.check_in(self.person))

    def test_check_in_method_working_as_intended(self):
        self.person.membership = True
        self.person.has_clean_shoes = True

        expected_result = "Bogdan checked in successfully!"
        self.assertEqual(expected_result, self.gym.check_in(self.person))
        self.assertEqual([self.person], self.gym.currently_in)

    def test_activate_membership_when_it_is_already_activated(self):
        self.person.membership = True

        self.assertEqual("Bogdan's membership is already active.",
                         self.gym.activate_membership(self.person))

    def test_activate_membership_working_as_intended(self):
        self.person.membership = False

        self.assertEqual("Bogdan's membership is now active.",
                         self.gym.activate_membership(self.person))
        self.assertEqual(True, self.person.membership)

    def test_status_method_when_the_gym_is_empty(self):
        expected_result = 'Muscle Power\n' \
                          'There is no one inside at the moment.'
        self.assertEqual(expected_result, self.gym.status())

    def test_status_method_when_there_are_people_inside_the_gym(self):
        person1 = Person('Maria', 21, 'female', True)
        person2 = Person('George', 30, 'male', True)
        person3 = Person('Natasha', 25, 'female', True)
        person4 = Person('Ivan', 27, 'male', True)

        self.gym.currently_in = [self.person, person1, person2, person3, person4]

        expected_result = 'Muscle Power\n' \
                          'People inside the gym: 5/100\n' \
                          'Their average age: 25.2\n' \
                          'Females: 2\n' \
                          'Males: 3'
        self.assertEqual(expected_result, self.gym.status())


if __name__ == '__main__':
    main()
