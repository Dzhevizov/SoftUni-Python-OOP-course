from unittest import TestCase, main

from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def setUp(self):
        self.pet_shop = PetShop('Privet')

    def test_init_should_create_instance(self):
        self.assertEqual('Privet', self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_when_quantity_is_negative_or_equal_to_zero_should_raise(self):
        test_quantities = [-5, 0]
        for quantity in test_quantities:
            with self.assertRaises(ValueError) as context:
                self.pet_shop.add_food('food', quantity)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food_when_quantity_is_positive_and_food_not_exist(self):
        food = 'food'
        quantity = 5
        actual = self.pet_shop.add_food(food, quantity)
        expected = f"Successfully added {quantity:.2f} grams of {food}."

        self.assertEqual(expected, actual)
        self.assertIn(food, self.pet_shop.food)
        self.assertEqual(quantity, self.pet_shop.food[food])

    def test_add_food_when_quantity_is_positive_and_food_exist(self):
        food = 'food'
        quantity = 5
        self.pet_shop.add_food(food, quantity)
        actual = self.pet_shop.add_food(food, quantity)
        expected = f"Successfully added {quantity:.2f} grams of {food}."

        self.assertEqual(expected, actual)
        self.assertIn(food, self.pet_shop.food)
        self.assertEqual(quantity * 2, self.pet_shop.food[food])

    def test_add_pet_when_name_not_exist_should_add(self):
        pet = 'Toni'
        actual = self.pet_shop.add_pet(pet)
        expected = f'Successfully added {pet}.'

        self.assertEqual(expected, actual)
        self.assertIn(pet, self.pet_shop.pets)

    def test_add_pet_when_name_already_exist_should_raise(self):
        pet = 'Toni'
        self.pet_shop.add_pet(pet)

        with self.assertRaises(Exception) as context:
            self.pet_shop.add_pet(pet)

        self.assertEqual('Cannot add a pet with the same name', str(context.exception))

    def test_feed_pet_when_pet_not_exist__should_raise(self):
        food = 'food'
        pet = 'Toni'
        with self.assertRaises(Exception) as context:
            self.pet_shop.feed_pet(food, pet)

        self.assertEqual('Please insert a valid pet name', str(context.exception))

    def test_feed_pet_when_pet_exist_but_food_does_not(self):
        food = 'food'
        pet = 'Toni'
        self.pet_shop.add_pet(pet)

        actual = self.pet_shop.feed_pet(food, pet)
        expected = f'You do not have {food}'

        self.assertEqual(expected, actual)

    def test_feed_pet_when_pet_exist_and_food_quantity_is_less_than_100(self):
        food = 'food'
        pet = 'Toni'
        quantity = 5
        self.pet_shop.add_pet(pet)
        self.pet_shop.add_food(food, quantity)

        actual = self.pet_shop.feed_pet(food, pet)
        expected = f'Adding food...'

        self.assertEqual(expected, actual)
        self.assertEqual(quantity + 1000, self.pet_shop.food[food])

    def test_feed_pet_when_pet_exist_and_food_quantity_is_equal_or_more_than_100(self):
        food = 'food'
        pet = 'Toni'
        test_quantity = [100, 200]
        self.pet_shop.add_pet(pet)
        for quantity in test_quantity:
            self.pet_shop.add_food(food, quantity)

            actual = self.pet_shop.feed_pet(food, pet)
            expected = f'{pet} was successfully fed'

            self.assertEqual(expected, actual)
            self.assertEqual(quantity - 100, self.pet_shop.food[food])

    def test_repr_should_return_proper_string(self):
        actual = str(self.pet_shop)
        expected = f'Shop {self.pet_shop.name}:\n' \
                   f'Pets: {", ".join(self.pet_shop.pets)}'

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
