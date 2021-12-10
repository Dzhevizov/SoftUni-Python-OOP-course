class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if self.capacity - sum([x.capacity_consumption for x in self.software_components]) >= software.capacity_consumption \
                and self.memory - sum([x.memory_consumption for x in self.software_components]) >= software.memory_consumption:
            self.software_components.append(software)
        else:
            raise Exception('Software cannot be installed')

    def uninstall(self, software):

        self.software_components.remove(software)
