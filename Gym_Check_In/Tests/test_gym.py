from unittest import TestCase, main
from Gym_Check_In.gym import Gym


class GymTests(TestCase):
    def setUp(self):
        self.gym = Gym('Muscle Power', 100)

    def test_constructor(self):
        self.assertEqual('Muscle Power', self.gym.gym_name)
        self.assertEqual(100, self.gym.max_capacity)
        self.assertEqual([], self.gym.currently_in)


if __name__ == '__main__':
    main()
