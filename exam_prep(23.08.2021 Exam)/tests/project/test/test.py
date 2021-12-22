from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    name = 'name'
    author = 'author1'
    title = 'book1'
    title2 = 'book2'
    reader = 'reader'

    def setUp(self):
        self.library = Library(self.name)

    def test_init(self):
        self.assertEqual(self.name, self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_init_when_name_is_empty_string_should_raise(self):
        with self.assertRaises(ValueError) as context:
            library = Library('')

        expected = 'Name cannot be empty string!'
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_add_book_when_author_not_exists_should_add(self):
        self.library.add_book(self.author, self.title)

        self.assertIn(self.author, self.library.books_by_authors)
        self.assertEqual([self.title], self.library.books_by_authors[self.author])

    def test_add_book_when_author_exists_book_not_exists_should_add_book(self):
        self.library.add_book(self.author, self.title)
        self.library.add_book(self.author, self.title2)

        self.assertIn(self.author, self.library.books_by_authors)
        self.assertEqual([self.title, self.title2], self.library.books_by_authors[self.author])

    def test_add_book_when_author_and_book_exists_should_ignore(self):
        self.library.add_book(self.author, self.title)
        self.library.add_book(self.author, self.title)

        self.assertIn(self.author, self.library.books_by_authors)
        self.assertEqual([self.title], self.library.books_by_authors[self.author])

    def test_add_reader_when_reader_not_exists_should_add(self):
        expected = None
        actual = self.library.add_reader(self.reader)

        self.assertIn(self.reader, self.library.readers)
        self.assertEqual([], self.library.readers[self.reader])
        self.assertEqual(expected, actual)

    def test_add_reader_when_reader_exists_should_ignore_and_return_proper_message(self):
        self.library.add_reader(self.reader)

        expected = f'{self.reader} is already registered in the {self.name} library.'
        actual = self.library.add_reader(self.reader)

        self.assertIn(self.reader, self.library.readers)
        self.assertEqual([], self.library.readers[self.reader])
        self.assertEqual(expected, actual)

    def test_rent_book_when_reader_not_exists(self):
        expected = f"{self.reader} is not registered in the {self.name} Library."
        actual = self.library.rent_book(self.reader, self.author, self.title)

        self.assertEqual(expected, actual)

    def test_rent_book_when_author_not_exists(self):
        self.library.add_reader(self.reader)

        expected = f"{self.name} Library does not have any {self.author}'s books."
        actual = self.library.rent_book(self.reader, self.author, self.title)

        self.assertEqual(expected, actual)

    def test_rent_book_when_book_not_exists(self):
        self.library.add_reader(self.reader)
        self.library.add_book(self.author, self.title)

        expected = f"""{self.name} Library does not have {self.author}'s "{self.title2}"."""
        actual = self.library.rent_book(self.reader, self.author, self.title2)

        self.assertEqual(expected, actual)

    def test_rent_book_when_reader_author_and_book_exists(self):
        self.library.add_reader(self.reader)
        self.library.add_book(self.author, self.title)

        expected = None
        actual = self.library.rent_book(self.reader, self.author, self.title)

        self.assertEqual(expected, actual)
        self.assertIn(self.reader, self.library.readers)
        self.assertEqual([{self.author: self.title}], self.library.readers[self.reader])
        self.assertNotIn(self.title, self.library.books_by_authors[self.author])
        self.assertEqual([], self.library.books_by_authors[self.author])


if __name__ == '__main__':
    main()
