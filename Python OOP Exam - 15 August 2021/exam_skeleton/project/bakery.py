from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0
        self.food_names = set()
        self.drinks_names = set()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError('Name cannot be empty string or white space!')
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        for food in self.food_menu:
            if food.name == name:
                raise Exception(f'{food_type} {name} is already in the menu!')

        __possible_types = ['Bread', 'Cake']
        __food = None

        if food_type == __possible_types[0]:
            __food = Bread(name, price)
        elif food_type == __possible_types[1]:
            __food = Cake(name, price)
        self.food_menu.append(__food)
        self.food_names.add(__food.name)
        return f'Added {name} ({food_type}) to the food menu'

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f'{drink_type} {name} is already in the menu!')

        __possible_types = ['Tea', 'Water']
        __drink = None

        if drink_type == __possible_types[0]:
            __drink = Tea(name, portion, brand)
        elif drink_type == __possible_types[1]:
            __drink = Water(name, portion, brand)
        self.drinks_menu.append(__drink)
        self.drinks_names.add(__drink.name)
        return f'Added {name} ({brand}) to the drink menu'

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f'Table {table_number} is already in the bakery!')

        __possible_types = ['InsideTable', 'OutsideTable']
        __table = None

        if table_type == __possible_types[0]:
            __table = InsideTable(table_number, capacity)
        elif table_type == __possible_types[1]:
            __table = OutsideTable(table_number, capacity)
        self.tables_repository.append(__table)
        return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f'Table {table.table_number} has been reserved for {number_of_people} people'
        return f'No available table for {number_of_people} people'

    def order_food(self, table_number: int, *args):
        __table_list = [x for x in self.tables_repository if x.table_number == table_number]
        if len(__table_list) == 0:
            return f'Could not find table {table_number}'

        table = __table_list[0]

        __food_in_menu = [x for x in args if x in self.food_names]
        __food_not_in_menu = [x for x in args if x not in self.food_names]
        __foods = []

        for food_name in __food_in_menu:
            for food in self.food_menu:
                if food.name == food_name:
                    __foods.append(food)

        for food in __foods:
            table.order_food(food)

        __food_in_menu_str = '\n'.join([repr(food) for food in __foods])
        __food_not_in_menu_str = '\n'.join(__food_not_in_menu)

        result = f"Table {table_number} ordered:" + "\n" +\
                 __food_in_menu_str + "\n" +\
                 f"{self.name} does not have in the menu:" + "\n" +\
                 __food_not_in_menu_str

        return result

    def order_drink(self, table_number: int, *args):
        __table_list = [x for x in self.tables_repository if x.table_number == table_number]
        if len(__table_list) == 0:
            return f'Could not find table {table_number}'

        table = __table_list[0]

        __drinks_in_menu = [x for x in args if x in self.drinks_names]
        __drinks_not_in_menu = [x for x in args if x not in self.drinks_names]
        __drinks = []

        for drink_name in __drinks_in_menu:
            for drink in self.drinks_menu:
                if drink.name == drink_name:
                    __drinks.append(drink)

        for drink in __drinks:
            table.order_drink(drink)

        __drinks_in_menu_str = '\n'.join([repr(drink) for drink in __drinks])
        __drinks_not_in_menu_str = '\n'.join(__drinks_not_in_menu)

        result = f"Table {table_number} ordered:" + "\n" +\
                 __drinks_in_menu_str + "\n" +\
                 f"{self.name} does not have in the menu:" + "\n" +\
                 __drinks_not_in_menu_str

        return result

    def leave_table(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                __bill = table.get_bill()
                self.total_income += __bill
                table.clear()
                result = [
                    f'Table: {table_number}',
                    f'Bill: {__bill:.2f}'
                ]
                return '\n'.join(result)

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            if not table.is_reserved:
                result.append(table.free_table_info())
        return '\n'.join(result)

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'
