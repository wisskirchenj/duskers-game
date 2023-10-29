from duskers.animation import Animation
from duskers.explorer import Explorer
from duskers.menu import Menu, EXIT, LOOP, TWO_UP, UP
from duskers.score_manager import ScoreManager
from duskers.state_manager import StateManager

NOT_ENOUGH_TITANIUM = 'Not enough titanium!'
MENU = '''                          |==========================|
                          |            MENU          |
                          |                          |
                          | [Back] to game           |
                          | Return to [Main] Menu    |
                          | [Save] and exit          |
                          | [Exit] game              |
                          |==========================|'''
UPGRADE_MENU = '''                       |================================|
                       |          UPGRADE STORE         |
                       |                         Price  |
                       | [1] Titanium Scan         250  |
                       | [2] Enemy Encounter Scan  500  |
                       | [3] New Robot            1000  |
                       |                                |
                       | [Back]                         |
                       |================================|'''
GAME_OVER = '''Enemy encounter!!!
Mission aborted, the last robot lost...
                        |==============================|
                        |          GAME OVER!          |
                        |==============================|'''

class Game:

    def __init__(self, animation: Animation, locations: list[str], player: str, titanium=0, robots=3, upgrades=''):
        self.animation = animation
        self.locations = locations
        self.player = player
        self.titanium = titanium
        self.robots = robots
        self.upgrades = upgrades

    def run(self) -> int:
        result = LOOP
        while result < UP:
            result = Menu(self.hub(), {"ex": self.explore, "up": self.upgrade,
                                       "save": self.save, "m": self.menu}).run_once()
        return EXIT if result == EXIT else result - 1

    def menu(self) -> int:
        return Menu(MENU, {"back": lambda: LOOP, "main": lambda: TWO_UP,
                           "save": lambda: self.save() or EXIT, "exit": exit_}).run_once()

    def save(self) -> int:
        StateManager(self.player, self.titanium, self.robots, self.upgrades).save()
        return LOOP

    def explore(self) -> int:
        titanium_found, encounter = Explorer(self.animation, self.locations, self.upgrades, self.robots).explore()
        self.titanium += titanium_found
        if encounter:
            self.robots -= 1
        if self.robots == 0:
            self.game_over()
            return TWO_UP
        return LOOP

    def upgrade(self) -> int:
        return Menu(UPGRADE_MENU, {"back": lambda: UP, "1": self.titanium_scan,
                    "2": self.enemy_info, "3": self.purchase_robot}).loop()

    def titanium_scan(self) -> int:
        if self.titanium < 250:
            print(NOT_ENOUGH_TITANIUM)
            return LOOP
        self.titanium -= 250
        self.upgrades += 'T'
        print('Purchase successful. You can now see how much titanium you can get from each found location.')
        return UP

    def enemy_info(self) -> int:
        if self.titanium < 500:
            print(NOT_ENOUGH_TITANIUM)
            return LOOP
        self.titanium -= 500
        self.upgrades += 'E'
        print('Purchase successful. '
              'You will now see how likely you will encounter an enemy at each found location.')
        return UP

    def purchase_robot(self) -> int:
        if self.titanium < 1000:
            print(NOT_ENOUGH_TITANIUM)
            return LOOP
        self.titanium -= 1000
        self.robots += 1
        print('Purchase successful. You now have an additional robot')
        return UP

    def hub(self):
        return '+==============================================================================+\n' + \
            '  $   $$$$$$$   $  |' * (self.robots - 1) + '  $   $$$$$$$   $\n' + \
            '  $$$$$     $$$$$  |' * (self.robots - 1) + '  $$$$$     $$$$$\n' + \
            '      $$$$$$$      |' * (self.robots - 1) + '      $$$$$$$\n' + \
            '     $$$   $$$     |' * (self.robots - 1) + '     $$$   $$$\n' + \
            '     $       $     |' * (self.robots - 1) + '     $       $\n' + \
            f'''+==============================================================================+
| Titanium: {self.titanium:<67}|
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+'''

    def game_over(self):
        print(GAME_OVER)
        ScoreManager().add_score(self.player, self.titanium)


def exit_() -> int:
    print('Thanks for playing, bye!')
    return EXIT
