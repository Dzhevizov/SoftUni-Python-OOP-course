from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    hero_name = 'Artas'
    hero_level = 10
    hero_health = 100
    hero_damage = 60
    enemy_name = 'Ilidan'
    enemy_level = 1
    enemy_health = 70
    enemy_damage = 50

    def setUp(self):
        self.hero = Hero(self.hero_name, self.hero_level, self.hero_health, self.hero_damage)
        self.enemy_hero = Hero(self.enemy_name, self.enemy_level, self.enemy_health, self.enemy_damage)


    def test_init__should_create_instance(self):
        self.assertEqual(self.hero_name, self.hero.username)
        self.assertEqual(self.hero_level, self.hero.level)
        self.assertEqual(self.hero_health, self.hero.health)
        self.assertEqual(self.hero_damage, self.hero.damage)

    def test_battle__when_username_is_equal_to_enemy_name__expect_to_raise(self):
        self.enemy_hero.username = self.hero.username

        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy_hero)

        self.assertEqual('You cannot fight yourself', str(context.exception))

    def test_battle__when_hero_health_is_negative_or_zero__expect_to_raise(self):
        test_health = [-10, 0]
        for self.hero.health in test_health:
            with self.assertRaises(ValueError) as context:
                self.hero.battle(self.enemy_hero)

        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(context.exception))

    def test_battle__when_enemy_hero_health_is_negative_or_zero__expect_to_raise(self):
        test_health = [-10, 0]
        for self.enemy_hero.health in test_health:
            with self.assertRaises(ValueError) as context:
                self.hero.battle(self.enemy_hero)

        self.assertEqual(f'You cannot fight {self.enemy_hero.username}. He needs to rest', str(context.exception))

    def test_battle__when_both_heroes_have_same_attributes__expect_to_return_Draw(self):
        self.enemy_hero.level = self.hero.level
        self.enemy_hero.health = self.hero.health
        self.enemy_hero.damage = self.hero.damage

        expected_result = 'Draw'
        actual_result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(self.hero_health - self.enemy_hero.damage * self.enemy_hero.level, self.hero.health)

    def test_battle__when_hero_wins__should_add_bonuses_and_return_proper_string(self):
        expected_result = 'You win'
        actual_result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(self.hero_level + 1, self.hero.level)
        self.assertEqual(self.hero_health - self.enemy_damage * self.enemy_level + 5, self.hero.health)
        self.assertEqual(self.hero_damage + 5, self.hero.damage)

    def test_battle__when_hero_loses__should_add_bonuses_and_return_proper_string(self):
        expected_result = 'You lose'
        actual_result = self.enemy_hero.battle(self.hero)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(self.hero_level + 1, self.hero.level)
        self.assertEqual(self.hero_health - self.enemy_damage * self.enemy_level + 5, self.hero.health)
        self.assertEqual(self.hero_damage + 5, self.hero.damage)

    def test_str__should_return_proper_string(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"

        actual_result = str(self.hero)

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
