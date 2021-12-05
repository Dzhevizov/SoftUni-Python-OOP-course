from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.cat = Mammal('Toni', 'Cat', 'meow')

    def test_init__expect_to_create_instance(self):
        self.assertEqual('Toni', self.cat.name)
        self.assertEqual('Cat', self.cat.type)
        self.assertEqual('meow', self.cat.sound)
        self.assertEqual("animals", self.cat._Mammal__kingdom)

    def test_make_sound__expect_to_return_correct_message(self):
        self.assertEqual(f"{self.cat.name} makes {self.cat.sound}", self.cat.make_sound())

    def test_info__expect_to_return_correct_message(self):
        self.assertEqual(f"{self.cat.name} is of type {self.cat.type}", self.cat.info())

    def test_get_kingdom__expect_to_return_kingdom_value(self):
        self.assertEqual("animals", self.cat.get_kingdom())


if __name__ == '__main__':
    main()
