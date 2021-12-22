from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    __successful_missions = 0
    __not_completed_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        __valid_astronaut_types = ["Biologist", "Geodesist", "Meteorologist"]
        if astronaut_type == __valid_astronaut_types[0]:
            astronaut = Biologist(name)
        elif astronaut_type == __valid_astronaut_types[1]:
            astronaut = Geodesist(name)
        elif astronaut_type == __valid_astronaut_types[2]:
            astronaut = Meteorologist(name)
        else:
            raise Exception('Astronaut type is not valid!')

        if self.astronaut_repository.find_by_name(name):
            return f'{name} is already added.'

        self.astronaut_repository.add(astronaut)
        return f'Successfully added {astronaut_type}: {name}.'

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f'{name} is already added.'

        planet = Planet(name)
        for item in items.split(', '):
            planet.items.append(item)

        self.planet_repository.add(planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f'Astronaut {name} doesn\'t exist!')

        self.astronaut_repository.remove(astronaut)
        return f'Astronaut {name} was retired!'

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception('Invalid planet name!')

        sorted_astronauts = sorted(self.astronaut_repository.astronauts, key=lambda x: x.oxygen, reverse=True)
        suitable_astronauts = [x for x in sorted_astronauts[:5] if x.oxygen > 30]

        if not suitable_astronauts:
            raise Exception('You need at least one astronaut to explore the planet!')

        is_successful = False
        participants = 0

        for astronaut in suitable_astronauts:
            participants += 1

            while planet.items:
                item = planet.items.pop()
                astronaut.backpack.append(item)
                astronaut.breathe()
                if astronaut.oxygen <= 0:
                    break

            if not planet.items:
                is_successful = True
                break

        if is_successful:
            self.__successful_missions += 1
            return f'Planet: {planet_name} was explored. {participants} astronauts participated in collecting items.'

        self.__not_completed_missions += 1
        return 'Mission is not completed.'

    def report(self):
        result = [f'{self.__successful_missions} successful missions!',
                  f'{self.__not_completed_missions} missions were not completed!', 'Astronauts\' info:']

        for astronaut in self.astronaut_repository.astronauts:
            result.append(f'Name: {astronaut.name}')
            result.append(f'Oxygen: {astronaut.oxygen}')
            if not astronaut.backpack:
                result.append(f'Backpack items: none')
            else:
                result.append(f'Backpack items: {", ".join(astronaut.backpack)}')

        return '\n'.join(result)
