from project.car.car import Car


class MuscleCar(Car):
    _min_speed_limit = 250
    _max_speed_limit = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)
