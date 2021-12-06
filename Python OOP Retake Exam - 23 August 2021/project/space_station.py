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

        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return f'{name} is already added.'

        if astronaut_type == __valid_astronaut_types[0]:
            astronaut = Biologist(name)
        elif astronaut_type == __valid_astronaut_types[1]:
            astronaut = Geodesist(name)
        elif astronaut_type == __valid_astronaut_types[2]:
            astronaut = Meteorologist(name)
        else:
            raise Exception('Astronaut type is not valid!')

        self.astronaut_repository.add(astronaut)
        return f'Successfully added {astronaut_type}: {name}.'

    def add_planet(self, name: str, items: str):
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return f'{name} is already added.'

        items_list = items.split(', ')
        planet = Planet(name)
        planet.items = items_list
        self.planet_repository.add(planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                self.astronaut_repository.remove(astronaut)
                return f'Astronaut {name} was retired!'

        raise Exception(f'Astronaut {name} doesn\'t exist!')

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        for planet in self.planet_repository.planets:
            if planet.name == planet_name:

                __sorted_astronauts = sorted(self.astronaut_repository.astronauts, key=lambda x: x.oxygen, reverse=True)
                if len(__sorted_astronauts) > 5:
                    __chosen_astronauts = [x for x in __sorted_astronauts[:5] if x.oxygen > 30]
                else:
                    __chosen_astronauts = [x for x in __sorted_astronauts if x.oxygen > 30]

                if len(__chosen_astronauts) == 0:
                    raise Exception('You need at least one astronaut to explore the planet!')

                index = 0

                for item in reversed(planet.items):
                    if index == len(__chosen_astronauts):
                        break
                    for astronaut in self.astronaut_repository.astronauts:
                        if astronaut.name == __chosen_astronauts[index].name:
                            astronaut.backpack.append(item)
                            planet.items.remove(item)
                            astronaut.breathe()

                            if astronaut.oxygen <= 0:
                                index += 1

                            break

                if len(planet.items) == 0:
                    self.__successful_missions += 1
                    return f'Planet: {planet_name} was explored. ' \
                           f'{index + 1} astronauts participated in collecting items.'
                else:
                    self.__not_completed_missions += 1
                    return 'Mission is not completed.'

        raise Exception('Invalid planet name!')

    def report(self):
        result = [f'{self.__successful_missions} successful missions!',
                  f'{self.__not_completed_missions} missions were not completed!',
                  f'Astronauts\' info:']
        for astronaut in self.astronaut_repository.astronauts:
            result.append(f'Name: {astronaut.name}')
            result.append(f'Oxygen: {astronaut.oxygen}')
            if astronaut.backpack:
                result.append(f'Backpack items: {", ".join(astronaut.backpack)}')
            else:
                result.append('Backpack items: none')

        return '\n'.join(result)
