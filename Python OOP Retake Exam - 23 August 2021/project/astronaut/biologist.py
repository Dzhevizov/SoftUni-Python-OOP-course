from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    __oxygen_needs = 5

    def __init__(self, name):
        super().__init__(name, 70)

    def breathe(self):
        self.oxygen -= self.__oxygen_needs
