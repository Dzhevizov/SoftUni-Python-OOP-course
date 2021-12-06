from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    __oxygen_needs = 15

    def __init__(self, name):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= self.__oxygen_needs
