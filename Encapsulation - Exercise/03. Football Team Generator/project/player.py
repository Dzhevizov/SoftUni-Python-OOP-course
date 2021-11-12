class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be empty string")
        self.__name = value

    def __str__(self):
        result = f"Player: {self.name}\nSprint: {self.__sprint}\nDribble: {self.__dribble}\n" \
                 f"Passing: {self.__passing}\nShooting: {self.__shooting}"
        return result

