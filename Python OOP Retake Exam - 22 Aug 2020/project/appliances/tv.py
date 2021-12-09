from project.appliances.appliance import Appliance


class TV(Appliance):
    __cost = 1.5

    def __init__(self):
        super().__init__(self.__cost)
