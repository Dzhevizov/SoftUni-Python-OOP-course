from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    __capacity = 50

    def __init__(self, name):
        super().__init__(name, self.__capacity)

    def add_fish(self, fish):
        __valid_fish_types = ["FreshwaterFish", "SaltwaterFish"]
        if len(self.fish) == self.capacity:
            return 'Not enough capacity.'

        if fish.__class__.__name__ == __valid_fish_types[0]:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

        elif fish.__class__.__name__ == __valid_fish_types[1]:
            return 'Water not suitable.'
