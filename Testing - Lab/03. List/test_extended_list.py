from extended_list import IntegerList

from unittest import TestCase, main


class TestIntegerList(TestCase):
    def test_init__when_all_args_are_valid__expect_to_be_added_in_the_list(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        expected_result = [1, 2, 3, 4, 5]
        actual_result = test_list.get_data()

        self.assertEqual(expected_result, actual_result)

    def test_init__when_one_arg_is_string__the_string_should_not_be_added_in_the_list(self):
        test_list = IntegerList(1, 2, 3, 4, 'PESHO')
        expected_result = [1, 2, 3, 4]
        actual_result = test_list.get_data()

        self.assertEqual(expected_result, actual_result)

    def test_add__when_element_is_string__expect_to_raise_ValueError(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        with self.assertRaises(ValueError) as context:
            test_list.add('PESHO')

        self.assertEqual('Element is not Integer', str(context.exception))

    def test_add__when_element_is_int__expect_to_be_added_in_the_list(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        test_list.add(6)

        expected_result = [1, 2, 3, 4, 5, 6]
        actual_result = test_list.get_data()

        self.assertEqual(expected_result, actual_result)

    def test_remove_index__when_given_index_is_equal_or_bigger_than_len_of_list__expect_to_raise_IndexError(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        test_indexes = [5, 10]
        for index in test_indexes:
            with self.assertRaises(IndexError) as context:
                test_list.remove_index(index)

            self.assertEqual('Index is out of range', str(context.exception))

    def test_remove_index__with_valid_index__expect_to_remove_item_on_the_given_index(self):
        test_list = IntegerList(1, 2, 3, 4, 5)

        expected_removed_item = 1
        actual_removed_item = test_list.remove_index(0)

        expected_result = [2, 3, 4, 5]
        actual_result = test_list.get_data()

        self.assertEqual(expected_removed_item, actual_removed_item)
        self.assertEqual(expected_result, actual_result)

    def test_get__when_given_index_is_equal_or_bigger_than_len_of_list__expect_to_raise_IndexError(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        test_indexes = [5, 10]
        for index in test_indexes:
            with self.assertRaises(IndexError) as context:
                test_list.get(index)

            self.assertEqual('Index is out of range', str(context.exception))

    def test_get__with_valid_index__expect_to_return_item_on_the_given_index(self):
        test_list = IntegerList(1, 2, 3, 4, 5)

        expected_result = 1
        actual_result = test_list.get(0)

        self.assertEqual(expected_result, actual_result)

    def test_insert__when_given_index_is_equal_or_bigger_than_len_of_list__expect_to_raise_IndexError(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        test_indexes = [5, 10]
        for index in test_indexes:
            with self.assertRaises(IndexError) as context:
                test_list.insert(index, 5)

            self.assertEqual('Index is out of range', str(context.exception))

    def test_insert__when_index_is_valid_and_element_is_string__expect_to_raise_ValueError(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        with self.assertRaises(ValueError) as context:
            test_list.insert(2, 'PESHO')

        self.assertEqual('Element is not Integer', str(context.exception))

    def test_insert__when_index_is_valid_and_element_is_int__expect_to_insert_element_on_given_index(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        test_list.insert(2, 5)

        expected_result = [1, 2, 5, 3, 4, 5]
        actual_result = test_list.get_data()

        self.assertEqual(expected_result, actual_result)

    def test_get_biggest__when_all_elements_are_valid__expect_to_return_element_with_biggest_value(self):
        test_list = IntegerList(1, 2, 3, 4, 5)

        expected_result = 5
        actual_result = test_list.get_biggest()

        self.assertEqual(expected_result, actual_result)

    def test_get_index__with_valid_element__expect_to_return_the_index_of_element(self):
        test_list = IntegerList(1, 2, 3, 4, 5)

        expected_result = 2
        actual_result = test_list.get_index(3)

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
