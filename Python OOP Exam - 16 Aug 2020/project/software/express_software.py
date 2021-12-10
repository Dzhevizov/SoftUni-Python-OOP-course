from project.software.software import Software


class ExpressSoftware(Software):
    __type = "Express"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.__type, capacity_consumption, memory_consumption * 2)
