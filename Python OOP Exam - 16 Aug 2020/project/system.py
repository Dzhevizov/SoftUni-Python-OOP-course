from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:

    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def find_object_by_name(object_name, list_of_objects):
        for obj in list_of_objects:
            if obj.name == object_name:
                return obj
        return None

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.find_object_by_name(hardware_name, System._hardware)

        if not hardware:
            return 'Hardware does not exist'

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(express_software)
        except Exception:
            raise Exception('Software cannot be installed')

        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.find_object_by_name(hardware_name, System._hardware)

        if not hardware:
            return 'Hardware does not exist'

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(light_software)
        except Exception:
            raise Exception('Software cannot be installed')

        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.find_object_by_name(hardware_name, System._hardware)
        if hardware:
            software = System.find_object_by_name(software_name, hardware.software_components)
            if software:
                hardware.uninstall(software)
                System._software.remove(software)
            else:
                return 'Some of the components do not exist'
        else:
            return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        return f"System Analysis" '\n'\
               f"Hardware Components: {len(System._hardware)}" + '\n'\
               f"Software Components: {len(System._software)}" + '\n'\
               f"Total Operational Memory: {sum([x.memory_consumption for x in System._software])} / {sum([x.memory for x in System._hardware])}" + '\n'\
               f"Total Capacity Taken: {sum([x.capacity_consumption for x in System._software])} / {sum([x.capacity for x in System._hardware])}"

    @staticmethod
    def system_split():
        result = []
        for hardware in System._hardware:
            if len(hardware.software_components) > 0:
                result.append(f"Hardware Component - {hardware.name}" + '\n'
                              f"Express Software Components: {len([x for x in hardware.software_components if x.software_type == 'Express'])}" + '\n'
                              f"Light Software Components: {len([x for x in hardware.software_components if x.software_type == 'Light'])}" + '\n'
                              f"Memory Usage: {sum([x.memory_consumption for x in hardware.software_components])} / {hardware.memory}" + '\n'
                              f"Capacity Usage: {sum([x.capacity_consumption for x in hardware.software_components])} / {hardware.capacity}" + '\n'
                              f"Type: {hardware.hardware_type}" + '\n'
                              f"Software Components: {', '.join([x.name for x in hardware.software_components])}")
            else:
                result.append(f"Hardware Component - {hardware.name}" + '\n'
                              f"Express Software Components: {len([x for x in hardware.software_components if x.software_type == 'Express'])}" + '\n'
                              f"Light Software Components: {len([x for x in hardware.software_components if x.software_type == 'Light'])}" + '\n'
                              f"Memory Usage: {sum([x.memory_consumption for x in hardware.software_components])} / {hardware.memory}" + '\n'
                              f"Capacity Usage: {sum([x.capacity_consumption for x in hardware.software_components])} / {hardware.capacity}" + '\n'
                              f"Type: {hardware.hardware_type}" + '\n'
                              f"Software Components: 'None'")

        return '\n'.join(result)
