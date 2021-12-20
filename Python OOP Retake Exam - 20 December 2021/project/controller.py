class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        __added_players = []
        for arg in args:
            if arg not in self.players:
                self.players.append(arg)
                __added_players.append(arg.name)
        return f'Successfully added: {", ".join(__added_players)}'

    def add_supply(self, *args):
        for arg in args:
            self.supplies.append(arg)

    def find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def sustain(self, player_name: str, sustenance_type: str):
        valid_types = ['Food', 'Drink']
        if sustenance_type not in valid_types:
            return

        player = self.find_player_by_name(player_name)
        if not player.need_sustenance:
            return f'{player_name} have enough stamina.'

        valid_supplies = [x for x in self.supplies if x.__class__.__name__ == sustenance_type]
        if sustenance_type == 'Food' and not valid_supplies:
            raise Exception('There are no food supplies left!')
        if sustenance_type == 'Drink' and not valid_supplies:
            raise Exception('There are no drink supplies left!')

        supply = valid_supplies[-1]
        self.supplies.remove(supply)
        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        result = []
        first_player = self.find_player_by_name(first_player_name)
        if first_player.stamina == 0:
            result.append(f'Player {first_player_name} does not have enough stamina.')
        second_player = self.find_player_by_name(second_player_name)
        if second_player.stamina == 0:
            result.append(f'Player {second_player_name} does not have enough stamina.')

        if result:
            return '\n'.join(result)

        ordered_players = sorted([first_player, second_player], key=lambda x: x.stamina)
        ordered_players[1].stamina -= ordered_players[0].stamina / 2
        if ordered_players[0].stamina - ordered_players[1].stamina / 2 < 0:
            ordered_players[0].stamina = 0
            return f'Winner: {ordered_players[1].name}'
        else:
            ordered_players[0].stamina -= ordered_players[1].stamina / 2

        if ordered_players[0].stamina > ordered_players[1].stamina:
            return f'Winner: {ordered_players[0].name}'
        if ordered_players[1].stamina > ordered_players[0].stamina:
            return f'Winner: {ordered_players[1].name}'

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')
