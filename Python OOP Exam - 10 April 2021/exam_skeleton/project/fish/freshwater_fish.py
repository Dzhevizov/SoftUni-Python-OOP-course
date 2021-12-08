from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    __size = 3

    def __init__(self, name, species, price):
        super().__init__(name, species, self.__size, price)

    def eat(self):
        self.size += 3
