from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    name = 'Chaika'
    capacity = 500
    passenger = 'Pesho'

    def setUp(self):
        self.train = Train(self.name, self.capacity)

    def test_init__should_create_instance(self):
        self.assertEqual(self.name, self.train.name)
        self.assertEqual(self.capacity, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add__when_passenger_count_equals_capacity__should_raise(self):
        self.train.capacity = 0

        with self.assertRaises(ValueError) as context:
            self.train.add(self.passenger)

        expected = self.train.TRAIN_FULL
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_add__when_passenger_name_already_exists__should_raise(self):
        self.train.add(self.passenger)

        with self.assertRaises(ValueError) as context:
            self.train.add(self.passenger)

        expected = self.train.PASSENGER_EXISTS.format(self.passenger)
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_add__with_enough_capacity_and_passenger_not_exists__should_add(self):
        expected = self.train.PASSENGER_ADD.format(self.passenger)
        actual = self.train.add(self.passenger)

        self.assertEqual(expected, actual)
        self.assertIn(self.passenger, self.train.passengers)

    def test_remove_when_passenger_not_exists__should_raise(self):
        with self.assertRaises(ValueError) as context:
            self.train.remove(self.passenger)

        expected = self.train.PASSENGER_NOT_FOUND.format(self.passenger)
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_remove_when_passenger_exists__should_remove(self):
        self.train.add(self.passenger)

        expected = self.train.PASSENGER_REMOVED.format(self.passenger)
        actual = self.train.remove(self.passenger)

        self.assertEqual(expected, actual)
        self.assertNotIn(self.passenger, self.train.passengers)


if __name__ == '__main__':
    main()
