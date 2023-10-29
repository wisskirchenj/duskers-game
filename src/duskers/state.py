class State:

    def __init__(self, player: str, titanium: int, robots: int, upgrades: str, last_save: str):
        self.player = player
        self.titanium = titanium
        self.last_save = last_save
        self.upgrades = upgrades
        self.robots = robots

    def __str__(self):
        return (f'{self.player} Titanium: {self.titanium} Robots: {self.robots} Last save: {self.last_save} '
                f'Upgrades: {self.show_upgrades()}')

    def show_upgrades(self) -> str:
        upgrades = []
        if 'T' in self.upgrades:
            upgrades.append('titanium_scan')
        if 'E' in self.upgrades:
            upgrades.append('enemy_info')
        return ','.join(upgrades)
