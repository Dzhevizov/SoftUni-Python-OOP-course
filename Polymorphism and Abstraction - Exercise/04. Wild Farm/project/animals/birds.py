from project.animals.animal import Bird


class Owl(Bird):
    _eatable_food = ["Meat"]
    _weight_increasement = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    _eatable_food = ["Vegetable", "Fruit", "Meat", "Seed"]
    _weight_increasement = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"
