from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    __cake_portion = 245

    def __init__(self, name, price):
        super().__init__(name, self.__cake_portion, price)
