class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for room in self.rooms:
            result += room.room_cost + room.expenses
        return f"Monthly consumption: {result}$."

    def pay(self):
        result = []
        for room in self.rooms:
            __total_costs = room.room_cost + room.expenses
            if room.budget >= __total_costs:
                room.budget -= __total_costs
                result.append(f'"{room.family_name} paid {__total_costs}$ and have {room.budget}$ left.')
            else:
                result.append(f'{room.family_name} does not have enough budget and must leave the hotel.')
                self.rooms.remove(room)
        return '\n'.join(result)

    def status(self):
        result = []
        for room in self.rooms:
            result.append(f'Total population: {room.members_count}')
            result.append(f'{room.family_name} with {room.members_count} members. '
                          f'Budget: {room.budget}$, Expenses: {room.expenses}$')
            if len(room.children) > 0:
                for idx, child in enumerate(room.children):
                    result.append(f'--- Child {idx + 1} monthly cost: {child.cost * 30}$')
            if len(room.appliances) > 0:
                result.append(f'--- Appliances monthly cost: {room.calculate_expenses(room.appliances)}$')
                