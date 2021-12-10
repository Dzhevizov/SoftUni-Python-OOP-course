from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    name = 'Factory'
    capacity = 100
    valid_ingredients = ["white", "yellow", "blue", "green", "red"]
    valid_ingredient = 'red'
    invalid_ingredient = 'black'
    test_quantity = 10

    def setUp(self):
        self.factory = PaintFactory(self.name, self.capacity)

    def test_init_should_create_instance(self):
        self.assertEqual(self.name, self.factory.name)
        self.assertEqual(self.capacity, self.factory.capacity)
        self.assertEqual(self.valid_ingredients, self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.ingredients)

    def test_add_ingredient__when_product_type_not_in_valid_ingredients__should_raise(self):
        with self.assertRaises(TypeError) as context:
            self.factory.add_ingredient(self.invalid_ingredient, self.test_quantity)

        expected = f'Ingredient of type {self.invalid_ingredient} not allowed in {self.factory.__class__.__name__}'
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_add_ingredient__when_quantity_exceeds_capacity__should_raise(self):
        with self.assertRaises(ValueError) as context:
            self.factory.add_ingredient(self.valid_ingredient, self.capacity + 1)

        expected = f'Not enough space in factory'
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_add_ingredient__with_valid_type_and_quantity_type_not_in_ingredients__should_add(self):

        expected = None
        actual = self.factory.add_ingredient(self.valid_ingredient, self.test_quantity)

        self.assertEqual(expected, actual)
        self.assertIn(self.valid_ingredient, self.factory.ingredients)
        self.assertEqual(self.test_quantity, self.factory.ingredients[self.valid_ingredient])

    def test_add_ingredient__with_valid_type_and_quantity_and_type_in_ingredients__should_increase_quantity(self):
        self.factory.add_ingredient(self.valid_ingredient, self.test_quantity)

        expected = None
        actual = self.factory.add_ingredient(self.valid_ingredient, self.test_quantity)

        self.assertEqual(expected, actual)
        self.assertIn(self.valid_ingredient, self.factory.ingredients)
        self.assertEqual(self.test_quantity * 2, self.factory.ingredients[self.valid_ingredient])

    def test_remove_ingredient__when_ingredient_not_exists__should_raise(self):
        with self.assertRaises(KeyError) as context:
            self.factory.remove_ingredient(self.valid_ingredient, self.test_quantity)

        expected = "'No such ingredient in the factory'"
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_remove_ingredient__when_quantity_is_bigger_than_content__should_raise(self):
        self.factory.add_ingredient(self.valid_ingredient, self.test_quantity)
        with self.assertRaises(ValueError) as context:
            self.factory.remove_ingredient(self.valid_ingredient, self.test_quantity + 1)

        expected = "Ingredients quantity cannot be less than zero"
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_remove_ingredient__when_quantity_is_equal_or_less_than_content__should_decrease_quantity(self):
        test_quantities = [self.test_quantity, self.test_quantity - 1]
        for quantity in test_quantities:
            self.factory.add_ingredient(self.valid_ingredient, self.test_quantity)

            result = self.factory.remove_ingredient(self.valid_ingredient, quantity)

            expected_quantity = self.test_quantity - quantity
            expected_result = None

            self.assertEqual(expected_result, result)
            self.assertIn(self.valid_ingredient, self.factory.ingredients)
            self.assertEqual(expected_quantity, self.factory.ingredients[self.valid_ingredient])

    def test_products__should_return_value_of_ingredients(self):
        expected = {}
        actual = self.factory.products

        self.assertEqual(expected, actual)

    def test_repr__should_return_proper_string(self):
        expected = f"Factory name: {self.name} with capacity {self.capacity}.\n"
        actual = repr(self.factory)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
