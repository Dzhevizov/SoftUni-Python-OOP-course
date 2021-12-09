from unittest import TestCase, main

from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):
    student_name = 'Pesho'
    school_year = 5
    invalid_name = ''
    subject = 'math'
    grade = 5.50
    subject2 = 'biology'
    grade2 = 4
    grade3 = 5

    def setUp(self):
        self.student = StudentReportCard(self.student_name, self.school_year)

    def test_init__with_valid_values__should_create_instance(self):
        self.assertEqual(self.student_name, self.student.student_name)
        self.assertEqual(self.school_year, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_init__when_student_name_is_empty_string__should_raise(self):
        with self.assertRaises(ValueError) as context:
            student = StudentReportCard(self.invalid_name, self.school_year)

        expected = 'Student Name cannot be an empty string!'
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_init__when_school_year_is_less_than_1_or_bigger_than_12__should_raise(self):
        invalid_test_years = [0, 13]
        for year in invalid_test_years:
            with self.assertRaises(ValueError) as context:
                student = StudentReportCard(self.student_name, year)

            expected = 'School Year must be between 1 and 12!'
            actual = str(context.exception)

            self.assertEqual(expected, actual)

    def test_init__when_school_year_equals_1_or_12(self):
        valid_test_years = [1, 12]
        for year in valid_test_years:
            student = StudentReportCard(self.student_name, year)
            self.assertEqual(self.student_name, student.student_name)
            self.assertEqual(year, student.school_year)
            self.assertEqual({}, student.grades_by_subject)

    def test_add_grade__when_subject_not_exists(self):
        expected = None
        actual = self.student.add_grade(self.subject, self.grade)

        self.assertEqual(expected, actual)
        self.assertIsInstance(self.subject, str)
        self.assertIsInstance(self.grade, float)
        self.assertIn(self.subject, self.student.grades_by_subject)
        self.assertEqual({self.subject: [self.grade]}, self.student.grades_by_subject)

    def test_add_grade__when_subject_exists(self):
        expected = None
        self.student.add_grade(self.subject, self.grade)
        actual = self.student.add_grade(self.subject, self.grade)

        self.assertEqual(expected, actual)
        self.assertIsInstance(self.subject, str)
        self.assertIsInstance(self.grade, float)
        self.assertIn(self.subject, self.student.grades_by_subject)
        self.assertEqual({self.subject: [self.grade, self.grade]}, self.student.grades_by_subject)

    def test_average_grade_by_subject__when_there_are_no_subjects(self):
        expected = ''
        actual = self.student.average_grade_by_subject()

        self.assertEqual(expected, actual)

    def test_average_grade_by_subject__when_there_are_subjects(self):
        self.student.add_grade(self.subject, self.grade)
        self.student.add_grade(self.subject2, self.grade2)
        self.student.add_grade(self.subject2, self.grade3)
        expected = f"{self.subject}: {self.grade:.2f}\n" +\
                   f"{self.subject2}: {((self.grade2 + self.grade3) / 2):.2f}"
        actual = self.student.average_grade_by_subject()

        self.assertEqual(expected, actual)

    def test_average_grade_for_all_subjects__when_there_are_subjects(self):
        list_of_test_grades = [self.grade, self.grade2, self.grade3]
        self.student.add_grade(self.subject, self.grade)
        self.student.add_grade(self.subject2, self.grade2)
        self.student.add_grade(self.subject2, self.grade3)
        expected = f"Average Grade: {sum(list_of_test_grades)/ len(list_of_test_grades) :.2f}"
        actual = self.student.average_grade_for_all_subjects()

        self.assertEqual(expected, actual)

    def test_repr_should_return_proper_string(self):
        self.student.add_grade(self.subject, self.grade)
        self.student.add_grade(self.subject2, self.grade2)
        self.student.add_grade(self.subject2, self.grade3)

        expected = f"Name: {self.student.student_name}\n" \
                   f"Year: {self.student.school_year}\n" \
                   f"----------\n" \
                   f"{self.student.average_grade_by_subject()}\n" \
                   f"----------\n" \
                   f"{self.student.average_grade_for_all_subjects()}"

        actual = repr(self.student)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
