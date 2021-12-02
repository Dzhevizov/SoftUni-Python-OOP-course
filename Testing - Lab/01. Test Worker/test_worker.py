from worker import Worker

from unittest import TestCase, main


class WorkerTests(TestCase):
    valid_name = 'Pesho'
    valid_salary = 2000
    valid_energy = 100

    def setUp(self):
        self.test_worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

    def test_initialization__with_correct_name_salary_and_energy(self):
        self.assertEqual(self.valid_name, self.test_worker.name)
        self.assertEqual(self.valid_salary, self.test_worker.salary)
        self.assertEqual(self.valid_energy, self.test_worker.energy)

    def test_rest__expect_to_increase_energy_by_one(self):
        expected_result = self.valid_energy + 1
        self.test_worker.rest()
        actual_result = self.test_worker.energy
        self.assertEqual(expected_result, actual_result)

    def test_work__with_negative_or_equal_to_zero_energy_expect_to_raise_exception(self):
        test_energies = [-5, 0]
        for self.test_worker.energy in test_energies:
            with self.assertRaises(Exception) as context:
                self.test_worker.work()

            self.assertEqual('Not enough energy.', str(context.exception))

    def test_work__with_positive_energy__expect_to_increase_money_by_salary_and_decrease_energy_by_one(self):
        expected_money = self.test_worker.money + self.test_worker.salary
        expected_energy = self.test_worker.energy - 1

        self.test_worker.work()

        self.assertEqual(expected_money, self.test_worker.money)
        self.assertEqual(expected_energy, self.test_worker.energy)

    def test_get_info__with_correct_values__expect_to_return_proper_string(self):
        expected_result = f'{self.valid_name} has saved 0 money.'
        actual_result = self.test_worker.get_info()

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()


"""
Test if the worker is initialized with the correct name, salary, and energy
Test if the worker's energy is incremented after the rest method is called
Test if an error is raised if the worker tries to work with negative energy or equal to 0
Test if the worker's money is increased by his salary correctly after the work method is called
Test if the worker's energy is decreased after the work method is called	
Test if the get_info method returns the proper string with correct values
"""