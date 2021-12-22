from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        __valid_types = ["MuscleCar", "SportsCar"]
        if car_type not in __valid_types:
            return

        for car in self.cars:
            if car.model == model:
                raise Exception(f'Car {model} is already created!')

        if car_type == __valid_types[0]:
            car = MuscleCar(model, speed_limit)
        elif car_type == __valid_types[1]:
            car = SportsCar(model, speed_limit)

        self.cars.append(car)
        return f'{car_type} {model} is created.'

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f'Driver {driver_name} is already created!')

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f'Driver {driver_name} is created.'

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f'Race {race_name} is already created!')

        race = Race(race_name)
        self.races.append(race)
        return f'Race {race_name} is created.'

    def find_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    def find_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def find_car_by_type(self, car_type):
        valid_cars = [x for x in self.cars if x.__class__.__name__ == car_type and not x.is_taken]
        if len(valid_cars) > 0:
            return valid_cars[-1]

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.find_driver_by_name(driver_name)
        car = self.find_car_by_type(car_type)

        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')

        if not car:
            raise Exception(f'Car {car_type} could not be found!')

        if driver.car:
            old_car = driver.car
            driver.car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f'Driver {driver_name} changed his car from {old_car.model} to {car.model}.'

        if not driver.car:
            driver.car = car
            car.is_taken = True
            return f'Driver {driver_name} chose the car {car.model}.'

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.find_race_by_name(race_name)
        driver = self.find_driver_by_name(driver_name)

        if not race:
            raise Exception(f'Race {race_name} could not be found!')

        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')

        if not driver.car:
            raise Exception(f'Driver {driver_name} could not participate in the race!')

        if driver in race.drivers:
            return f'Driver {driver_name} is already added in {race_name} race.'

        race.drivers.append(driver)
        return f'Driver {driver_name} added in {race_name} race.'

    def start_race(self, race_name: str):
        race = self.find_race_by_name(race_name)

        if not race:
            raise Exception(f'Race {race_name} could not be found!')

        if len(race.drivers) < 3:
            raise Exception(f'Race {race_name} cannot start with less than 3 participants!')

        won_list = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)

        info = []

        for driver in won_list[0:3]:
            driver.number_of_wins += 1
            info.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return '\n'.join(info)
