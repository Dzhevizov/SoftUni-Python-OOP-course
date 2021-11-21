from project.animals.animal import Mammal


class Mouse(Mammal):
    _eatable_food = ["Vegetable", "Fruit"]
    _weight_increasement = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    _eatable_food = ["Meat"]
    _weight_increasement = 0.40
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    _eatable_food = ["Vegetable", "Meat"]
    _weight_increasement = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    _eatable_food = ["Meat"]
    _weight_increasement = 1.00

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"
