from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([x.comfort for x in self.decorations])

    @abstractmethod
    def add_fish(self, fish):
        __valid_fish_types = ["FreshwaterFish", "SaltwaterFish"]
        if len(self.fish) == self.capacity:
            return 'Not enough capacity.'

        if fish.__class__.__name in __valid_fish_types:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        if len(self.fish) == 0:
            return f"{self.name}:\n" \
                   f"Fish: none\n" \
                   f"Decorations: {len(self.decorations)}\n" \
                   f"Comfort: {self.calculate_comfort()}"
        else:
            return f"{self.name}:\n" \
                   f"Fish: {' '.join([x.name for x in self.fish])}\n" \
                   f"Decorations: {len(self.decorations)}\n" \
                   f"Comfort: {self.calculate_comfort()}"
