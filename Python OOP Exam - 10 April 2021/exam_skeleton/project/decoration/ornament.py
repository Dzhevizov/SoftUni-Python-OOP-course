from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    __comfort = 1
    __price = 5

    def __init__(self):
        super().__init__(self.__comfort, self.__price)
