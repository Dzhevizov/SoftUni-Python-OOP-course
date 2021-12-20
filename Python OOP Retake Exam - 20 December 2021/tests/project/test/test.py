from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    name = 'movie'
    year = 2005
    rating = 9.5
    actor = 'actor'
    actor2 = 'actor2'
    other_name = 'movie2'
    other_year = 2000
    lower_rating = 8.5
    higher_rating = 9.9

    def setUp(self):
        self.movie = Movie(self.name, self.year, self.rating)

    def test_init(self):
        self.assertEqual(self.name, self.movie.name)
        self.assertEqual(self.year, self.movie.year)
        self.assertEqual(self.rating, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_init_when_name_is_empty_string_should_raise(self):
        with self.assertRaises(ValueError) as context:
            movie = Movie("", self.year, self.rating)

        expected = 'Name cannot be an empty string!'
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_init_when_year_is_less_than_1887_should_raise(self):
        with self.assertRaises(ValueError) as context:
            movie = Movie(self.name, 1886, self.rating)

        expected = 'Year is not valid!'
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_add_actor_when_not_exists_should_add(self):
        expected = None
        actual = self.movie.add_actor(self.actor)

        self.assertEqual(expected, actual)
        self.assertIn(self.actor, self.movie.actors)
        self.assertEqual([self.actor], self.movie.actors)

    def test_add_actor_when_exists_should_ignore_and_return_message(self):
        self.movie.add_actor(self.actor)

        expected = f"{self.actor} is already added in the list of actors!"
        actual = self.movie.add_actor(self.actor)

        self.assertEqual(expected, actual)
        self.assertIn(self.actor, self.movie.actors)
        self.assertEqual([self.actor], self.movie.actors)

    def test_gt_when_rating_is_higher(self):
        other = Movie(self.other_name, self.other_year, self.lower_rating)

        expected = f'"{self.movie.name}" is better than "{other.name}"'
        actual = self.movie > other

        self.assertEqual(expected, actual)

    def test_gt_when_rating_is_lower(self):
        other = Movie(self.other_name, self.other_year, self.higher_rating)

        expected = f'"{other.name}" is better than "{self.movie.name}"'
        actual = self.movie > other

        self.assertEqual(expected, actual)

    def test_repr_should_return_proper_string(self):
        self.movie.add_actor(self.actor)
        self.movie.add_actor(self.actor2)
        expected = f"Name: {self.movie.name}\n" \
                   f"Year of Release: {self.movie.year}\n" \
                   f"Rating: {self.movie.rating:.2f}\n" \
                   f"Cast: {', '.join(self.movie.actors)}"
        actual = repr(self.movie)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
