from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        __valid_aquarium_types = ["FreshwaterAquarium", "SaltwaterAquarium"]
        if aquarium_type not in __valid_aquarium_types:
            return "Invalid aquarium type."

        if aquarium_type == __valid_aquarium_types[0]:
            aquarium = FreshwaterAquarium(aquarium_name)
        else:
            aquarium = SaltwaterAquarium(aquarium_name)

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        __valid_decoration_types = ["Ornament", "Plant"]
        if decoration_type not in __valid_decoration_types:
            return 'Invalid decoration type.'

        if decoration_type == __valid_decoration_types[0]:
            decoration = Ornament()
        else:
            decoration = Plant()

        self.decorations_repository.add(decoration)
        return f'Successfully added {decoration_type}.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if not decoration:
            return f'There isn\'t a decoration of type {decoration_type}.'
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.add_decoration(decoration)
                self.decorations_repository.remove(decoration)
                return f'Successfully added {decoration_type} to {aquarium_name}.'

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        __valid_fish_types = ["FreshwaterFish", "SaltwaterFish"]
        if fish_type not in __valid_fish_types:
            return f'There isn\'t a fish of type {fish_type}.'

        if fish_type == __valid_fish_types[0]:
            fish = FreshwaterFish(fish_name, fish_species, price)
        else:
            fish = SaltwaterFish(fish_name, fish_species, price)

        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                result = aquarium.add_fish(fish)
                return result

    def feed_fish(self, aquarium_name: str):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.feed()
                return f'Fish fed: {len(aquarium.fish)}'

    def calculate_value(self, aquarium_name: str):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                result = sum([x.price for x in aquarium.decorations]) + sum([x.price for x in aquarium.fish])
                return f'The value of Aquarium {aquarium_name} is {result:.2f}.'

    def report(self):
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))

        return "\n".join(result)
