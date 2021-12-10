import math

from project.software.software import Software


class LightSoftware(Software):
    __type = "Light"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.__type, math.floor(capacity_consumption * 1.5),
                         math.floor(memory_consumption * 0.5))
