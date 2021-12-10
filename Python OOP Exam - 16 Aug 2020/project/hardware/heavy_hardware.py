import math

from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    __type = "Heavy"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.__type, capacity * 2, math.floor(memory * 0.75))
