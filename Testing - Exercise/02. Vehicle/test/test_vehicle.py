from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(45.5, 117)

    def test_init__expect_to_create_instance(self):
        self.assertEqual(45.5, self.vehicle.fuel)
        self.assertEqual(45.5, self.vehicle.capacity)
        self.assertEqual(117, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive__when_fuel_not_enough_for_given_distance__expect_to_raise(self):
        self.vehicle.fuel = 0
        distance = 10

        with self.assertRaises(Exception) as context:
            self.vehicle.drive(distance)

        self.assertEqual('Not enough fuel', str(context.exception))

    def test_drive__when_fuel_is_enough__expect_to_reduce_fuel_by_needed_fuel(self):
        distance = 10
        needed_fuel = distance * self.vehicle.fuel_consumption

        expected_result = self.vehicle.fuel - needed_fuel

        self.vehicle.drive(distance)
        actual_result = self.vehicle.fuel

        self.assertEqual(expected_result, actual_result)

    def test_refuel__when_fuel_exceed_capacity__expect_to_raise(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(5)

        self.assertEqual('Too much fuel', str(context.exception))

    def test_refuel__when_fuel_does_not_exceed_capacity__expect_to_increase_fuel(self):
        self.vehicle.fuel = 10
        added_fuel = 10
        expected_result = self.vehicle.fuel + added_fuel

        self.vehicle.refuel(10)
        actual_result = self.vehicle.fuel

        self.assertEqual(expected_result, actual_result)

    def test_str__should_return_proper_string(self):
        expected_result = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        actual_result = str(self.vehicle)

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
