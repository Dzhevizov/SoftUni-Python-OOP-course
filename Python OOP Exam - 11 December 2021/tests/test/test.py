from unittest import TestCase, main

from project.team import Team


class TestTeam(TestCase):
    valid_name = 'Cherry'
    invalid_name = 'Cherry101'
    player1 = 'Gosho'
    player1_age = 20
    player2 = 'Pesho'
    player2_age = 22

    def test_init__with_valid_name__should_create_instance(self):
        team = Team(self.valid_name)

        self.assertEqual(self.valid_name, team.name)
        self.assertEqual({}, team.members)

    def test_init__when_name_contains_numbers__should_raise(self):
        with self.assertRaises(ValueError) as context:
            team = Team(self.invalid_name)

        expected = 'Team Name can contain only letters!'
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_add_member_when_all_names_does_not_exists_in_members__should_add(self):
        team = Team(self.valid_name)
        players = {self.player1: self.player1_age, self.player2: self.player2_age}

        actual = team.add_member(**players)
        expected = f"Successfully added: {', '.join([f'{self.player1}, {self.player2}'])}"

        self.assertEqual(expected, actual)
        self.assertIn(self.player1, team.members)
        self.assertIn(self.player2, team.members)
        self.assertEqual(self.player1_age, team.members[self.player1])
        self.assertEqual(self.player2_age, team.members[self.player2])

    def test_add_member_when_one_name_exist_in_members__should_ignore(self):
        team = Team(self.valid_name)
        test_player = {self.player1: self.player1_age}
        team.add_member(**test_player)

        players = {self.player1: self.player1_age, self.player2: self.player2_age}

        actual = team.add_member(**players)
        expected = f"Successfully added: {', '.join([f'{self.player2}'])}"

        self.assertEqual(expected, actual)
        self.assertIn(self.player1, team.members)
        self.assertIn(self.player2, team.members)
        self.assertEqual(self.player1_age, team.members[self.player1])
        self.assertEqual(self.player2_age, team.members[self.player2])

    def test_remove_member__when_name_not_exists(self):
        team = Team(self.valid_name)

        actual = team.remove_member(self.player1)
        expected = f"Member with name {self.player1} does not exist"

        self.assertEqual(expected, actual)
        self.assertDictEqual({}, team.members)

    def test_remove_member__when_name_exists(self):
        team = Team(self.valid_name)
        test_player = {self.player1: self.player1_age}
        team.add_member(**test_player)

        actual = team.remove_member(self.player1)
        expected = f"Member {self.player1} removed"

        self.assertEqual(expected, actual)
        self.assertDictEqual({}, team.members)

    def test__gt__when_is_bigger(self):
        team = Team(self.valid_name)
        other_team = Team('Strawberry')

        test_player = {self.player1: self.player1_age}
        team.add_member(**test_player)

        self.assertEqual(True, team > other_team)

    def test__gt__when_is_less(self):
        team = Team(self.valid_name)
        other_team = Team('Strawberry')

        test_player = {self.player1: self.player1_age}
        team.add_member(**test_player)

        self.assertEqual(False, team < other_team)

    def test__gt__when_is_equal(self):
        team = Team(self.valid_name)
        other_team = Team('Strawberry')

        test_player = {self.player1: self.player1_age}
        team.add_member(**test_player)

        self.assertEqual(False, team == other_team)

    def test__len__should_return_count_of_members(self):
        team = Team(self.valid_name)
        test_player = {self.player1: self.player1_age}
        team.add_member(**test_player)

        self.assertEqual(1, len(team))

    def test__add__should_concatenate_name_and_add_other_members(self):
        team = Team(self.valid_name)
        test_player = {self.player1: self.player1_age}
        team.add_member(**test_player)

        other_team = Team('Strawberry')
        test_player2 = {self.player2: self.player2_age}
        other_team.add_member(**test_player2)

        new_team = team + other_team

        self.assertEqual(team.name + other_team.name, new_team.name)
        self.assertIn(self.player1, new_team.members)
        self.assertIn(self.player2, new_team.members)
        self.assertEqual(self.player1_age, new_team.members[self.player1])
        self.assertEqual(self.player2_age, new_team.members[self.player2])

    def test__str__should_return_proper_string(self):
        team = Team(self.valid_name)
        players = {self.player1: self.player1_age, self.player2: self.player2_age}
        team.add_member(**players)

        actual = str(team)
        expected = f"Team name: {team.name}" + '\n' + f"Member: {self.player2} - {self.player2_age}-years old" + "\n" + \
                   f"Member: {self.player1} - {self.player1_age}-years old"

        self.assertEqual(expected,  actual)

    def test__str__when_empty_should_return_proper_string(self):
        team = Team(self.valid_name)

        actual = str(team)
        expected = f"Team name: {team.name}"

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
