from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    __oxygen_needs = 10

    def __init__(self, name):
        super().__init__(name, 50)

    def breathe(self):
        self.oxygen -= self.__oxygen_needs
