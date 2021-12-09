from project.appliances.appliance import Appliance


class Laptop(Appliance):
    __cost = 1

    def __init__(self):
        super().__init__(self.__cost)
