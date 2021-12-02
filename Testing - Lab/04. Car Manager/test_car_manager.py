from car_manager import Car

from unittest import TestCase, main


class TestCar(TestCase):
    valid_make = 'Honda'
    valid_model = 'Civic'
    valid_fuel_consumption = 7
    valid_fuel_capacity = 45

    def setUp(self):
        self.car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

    def test_init__when_all_attributes_are_valid_expect_to_create_object(self):
        self.assertEqual(self.valid_make, self.car.make)
        self.assertEqual(self.valid_model, self.car.model)
        self.assertEqual(self.valid_fuel_consumption, self.car.fuel_consumption)
        self.assertEqual(self.valid_fuel_capacity, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter__with_empty_string__expect_to_raise(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_model_setter__with_empty_string__expect_to_raise(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_fuel_consumption_setter__with_negative_and_equal_to_zero_value__expect_to_raise(self):
        test_fuel_consumption = [-5, 0]
        for fuel in test_fuel_consumption:
            with self.assertRaises(Exception) as context:
                self.car.fuel_consumption = fuel

            self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_fuel_capacity_setter__with_negative_and_equal_to_zero_value__expect_to_raise(self):
        test_fuel_capacity = [-5, 0]
        for fuel in test_fuel_capacity:
            with self.assertRaises(Exception) as context:
                self.car.fuel_capacity = fuel

            self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_fuel_amount_setter__when_negative__expect_to_raise(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -5

            self.assertEqual("Fuel amount cannot be negative!", str(context.exception))

    def test_refuel__with_negative_and_equal_to_zero_value__expect_to_raise(self):
        test_fuel = [-5, 0]
        for fuel in test_fuel:
            with self.assertRaises(Exception) as context:
                self.car.refuel(fuel)

            self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_refuel__when_positive_and_exceed_capacity__expect_amount_be_equal_to_capacity(self):
        self.car.refuel(50)

        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    def test_refuel_when_positive_and_less_than_capacity__expect_to_add_fuel(self):
        self.car.refuel(20)

        self.assertEqual(20, self.car.fuel_amount)

    def test_drive_when_not_enough_fuel_for_given_distance__expect_to_raise(self):
        distance = 20

        with self.assertRaises(Exception) as context:
            self.car.drive(distance)

        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))

    def test_drive_when_fuel_is_enough_for_given_distance__expect_fuel_amount_be_reduced_by_needed_fuel(self):
        distance = 20
        needed_fuel = 1.4
        self.car.fuel_amount = 20

        expected_result = self.car.fuel_amount - needed_fuel

        self.car.drive(distance)

        actual_result = self.car.fuel_amount

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
