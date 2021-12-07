from project.drink.drink import Drink


class Tea(Drink):
    __tea_price = 2.50

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, self.__tea_price, brand)
