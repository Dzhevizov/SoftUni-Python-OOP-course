from project.car.car import Car


class SportsCar(Car):
    _min_speed_limit = 400
    _max_speed_limit = 600

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)
