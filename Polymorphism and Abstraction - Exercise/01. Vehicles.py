from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    __air_condition_consumption = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = (self.fuel_consumption + self.__air_condition_consumption) * distance
        if needed_fuel > self.fuel_quantity:
            return
        self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    __air_condition_consumption = 1.6
    __refuel_percentage = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = (self.fuel_consumption + self.__air_condition_consumption) * distance
        if needed_fuel > self.fuel_quantity:
            return
        self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        added_fuel = fuel * self.__refuel_percentage
        self.fuel_quantity += added_fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
