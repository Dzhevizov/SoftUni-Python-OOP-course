from cat import Cat

from unittest import TestCase, main


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat('Toni')

    def test_eat__when_not_fed__expect_to_increase_size_by_one_and_become_fed_and_sleepy(self):
        self.cat.eat()

        self.assertEqual(1, self.cat.size)
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

    def test_eat__when_fed__expect_to_raise_exception(self):
        self.cat.eat()
        with self.assertRaises(Exception) as context:
            self.cat.eat()

        self.assertEqual('Already fed.', str(context.exception))

    def test_sleep__when_not_fed__expect_to_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(context.exception))

    def test_sleep__when_fed__expect_not_be_sleepy(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertEqual(1, self.cat.size)
        self.assertTrue(self.cat.fed)
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()

"""
Cat's size is increased after eating
Cat is fed after eating
Cat cannot eat if already fed, raises an error
Cat cannot fall asleep if not fed, raises an error
Cat is not sleepy after sleeping

"""