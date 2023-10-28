class State:

    def __init__(self, player: str, titanium: int, last_save: str):
        self.player = player
        self.titanium = titanium
        self.last_save = last_save
        self.robots = 3

    def __str__(self):
        return f'{self.player} Titanium: {self.titanium} Robots: {self.robots} Last save: {self.last_save}'
