import math

from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    __type = "Power"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.__type, math.floor(capacity * 0.25), math.floor(memory * 1.75))
