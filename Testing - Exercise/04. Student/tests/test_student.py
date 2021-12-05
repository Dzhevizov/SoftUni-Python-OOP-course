from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student('Pesho', {'JAVA': ['OOP'], 'Python': ['Advanced']})

    def test_init__when_courses_is_None__should_be_empty_dict(self):
        student = Student('Pesho')

        self.assertEqual('Pesho', student.name)
        self.assertEqual({}, student.courses)

    def test_init__when_courses_is_given_dict__expect_to_initialize(self):
        self.assertEqual('Pesho', self.student.name)
        self.assertEqual({'JAVA': ['OOP'], 'Python': ['Advanced']}, self.student.courses)

    def test_enroll__when_course_name_in_courses_and_notes_are_empty_string(self):
        expected_result = 'Course already added. Notes have been updated.'
        expected_courses = {'JAVA': ['OOP'], 'Python': ['Advanced']}

        actual_result = self.student.enroll('JAVA', "")

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_courses, self.student.courses)

    def test_enroll__when_course_name_in_courses_and_notes_are_list_of_strings(self):
        actual_result = self.student.enroll('JAVA', ["Basic", "Web"])

        expected_result = 'Course already added. Notes have been updated.'
        expected_courses = {'JAVA': ['OOP', 'Basic', 'Web'], 'Python': ['Advanced']}

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_courses, self.student.courses)

    def test_enroll__when_course_name_not_in_courses_and_add_course_notes_is_empty_strings_or_equals_Y(self):
        options = ["Y", ""]

        for option in options:
            self.student = Student('Pesho', {'JAVA': ['OOP'], 'Python': ['Advanced']})
            actual_result = self.student.enroll('JS', ['Fundamentals', 'Advanced'], option)

            expected_result = 'Course and course notes have been added.'
            expected_courses = {'JAVA': ['OOP'], 'Python': ['Advanced'], 'JS': ['Fundamentals', 'Advanced']}

            self.assertEqual(expected_result, actual_result)
            self.assertEqual(expected_courses, self.student.courses)

    def test_enroll__when_course_name_not_in_courses_and_add_course_notes_is_not_empty_strings_or_not_equals_Y(self):
        options = ["N", "5"]

        for option in options:
            self.student = Student('Pesho', {'JAVA': ['OOP'], 'Python': ['Advanced']})
            actual_result = self.student.enroll('JS', ['Fundamentals', 'Advanced'], option)

            expected_result = 'Course has been added.'
            expected_courses = {'JAVA': ['OOP'], 'Python': ['Advanced'], 'JS': []}

            self.assertEqual(expected_result, actual_result)
            self.assertEqual(expected_courses, self.student.courses)

    def test_add_notes__when_course_does_not_exist__expect_to_raise(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes('JS', ['Basic', 'Web'])

        self.assertEqual('Cannot add notes. Course not found.', str(context.exception))

    def test_add_notes__when_course_exist_in_courses__expect_to_add_notes_and_return_message(self):
        actual_result = self.student.add_notes('JAVA', 'Basic')

        expected_result = 'Notes have been updated'
        expected_courses = {'JAVA': ['OOP', 'Basic'], 'Python': ['Advanced']}

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_courses, self.student.courses)

    def test_leave_course__when_course_does_not_exist__expect_to_raise(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course('JS')

        self.assertEqual('Cannot remove course. Course not found.', str(context.exception))

    def test_leave_course__when_course_exist_in_courses__expect_to_remove_course_and_return_message(self):
        actual_result = self.student.leave_course('JAVA')

        expected_result = 'Course has been removed'
        expected_courses = {'Python': ['Advanced']}

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_courses, self.student.courses)


if __name__ == '__main__':
    main()
