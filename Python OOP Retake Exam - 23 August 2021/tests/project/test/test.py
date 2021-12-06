from project.library import Library

from unittest import TestCase, main


class TestLibrary(TestCase):
    test_name = 'Library'
    test_author = 'author1'
    test_book = 'book1'
    test_book2 = 'book2'
    test_reader = 'Pesho'

    def setUp(self):
        self.library = Library(self.test_name)

    def test_init__with_valid_name__should_create_instance(self):
        self.assertEqual(self.test_name, self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_init_when_name_is_empty_string__expect_to_raise(self):
        with self.assertRaises(ValueError) as context:
            self.library = Library('')

        self.assertEqual('Name cannot be empty string!', str(context.exception))

    def test_add_book_when_author_not_in_books_by_authors(self):
        result = self.library.add_book(self.test_author, self.test_book)

        self.assertIn(self.test_author, self.library.books_by_authors)
        self.assertIn(self.test_book, self.library.books_by_authors[self.test_author])
        self.assertEqual({self.test_author: [self.test_book]}, self.library.books_by_authors)
        self.assertEqual(None, result)

    def test_add_book_when_author_exist_in_books_by_authors_but_book_does_not(self):
        self.library.add_book(self.test_author, self.test_book)

        result = self.library.add_book(self.test_author, self.test_book2)

        self.assertIn(self.test_author, self.library.books_by_authors)
        self.assertIn(self.test_book, self.library.books_by_authors[self.test_author])
        self.assertEqual({self.test_author: [self.test_book, self.test_book2]}, self.library.books_by_authors)
        self.assertEqual(None, result)

    def test_add_reader_when_not_registered(self):
        result = self.library.add_reader(self.test_reader)

        self.assertEqual({self.test_reader: []}, self.library.readers)
        self.assertIn(self.test_reader, self.library.readers)
        self.assertEqual(None, result)

    def test_add_reader_when_already_registered(self):

        self.library.add_reader(self.test_reader)

        result = self.library.add_reader(self.test_reader)
        expected = f"{self.test_reader} is already registered in the {self.library.name} library."

        self.assertEqual({self.test_reader: []}, self.library.readers)
        self.assertIn(self.test_reader, self.library.readers)
        self.assertEqual(expected, result)

    def test_rent_book_when_reader_name_not_in_readers(self):
        result = self.library.rent_book(self.test_reader, self.test_author, self.test_book)
        expected = f"{self.test_reader} is not registered in the {self.library.name} Library."

        self.assertEqual(expected, result)

    def test_rent_book_when_reader_exist_but_author_not_in_books_by_authors(self):
        self.library.add_reader(self.test_reader)
        result = self.library.rent_book(self.test_reader, self.test_author, self.test_book)
        expected = f"{self.library.name} Library does not have any {self.test_author}'s books."

        self.assertEqual(expected, result)

    def test_rent_book_when_reader_and_author_exist_but_the_book_does_not(self):
        self.library.add_reader(self.test_reader)
        self.library.add_book(self.test_author, self.test_book2)

        result = self.library.rent_book(self.test_reader, self.test_author, self.test_book)
        expected = f"""{self.library.name} Library does not have {self.test_author}'s "{self.test_book}"."""

        self.assertEqual(expected, result)

    def test_rent_book_when_reader_and_author_and_book_exist(self):
        self.library.add_reader(self.test_reader)
        self.library.add_book(self.test_author, self.test_book)
        self.library.add_book(self.test_author, self.test_book2)

        result = self.library.rent_book(self.test_reader, self.test_author, self.test_book)

        self.assertEqual(None, result)
        self.assertIn({self.test_author: self.test_book}, self.library.readers[self.test_reader])
        self.assertNotIn(self.test_book, self.library.books_by_authors[self.test_author])


if __name__ == '__main__':
    main()
