from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    __comfort = 5
    __price = 10

    def __init__(self):
        super().__init__(self.__comfort, self.__price)
