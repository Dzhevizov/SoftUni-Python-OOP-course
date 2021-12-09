from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, len(children) + 2)
        self.room_cost = 30
        self.children = list(children)
        self.appliances = []
        self.__add_appliances(self.appliances, len(children) + 2, TV(), Fridge(), Laptop())
        self.calculate_expenses(self.children, self.appliances)

    @staticmethod
    def __add_appliances(collection, number, *objects):
        for _ in range(number):
            for el in objects:
                collection.append(el)
