from duskers.animation import Animation
from duskers.explorer import Explorer
from duskers.menu import Menu, EXIT, LOOP, TWO_UP, UP
from duskers.state_manager import StateManager

MENU = '''                          |==========================|
                          |            MENU          |
                          |                          |
                          | [Back] to game           |
                          | Return to [Main] Menu    |
                          | [Save] and exit          |
                          | [Exit] game              |
                          |==========================|'''
STARTED = '''+==============================================================================+
  $   $$$$$$$   $  |  $   $$$$$$$   $  |  $   $$$$$$$   $
  $$$$$     $$$$$  |  $$$$$     $$$$$  |  $$$$$     $$$$$
      $$$$$$$      |      $$$$$$$      |      $$$$$$$
     $$$   $$$     |     $$$   $$$     |     $$$   $$$
     $       $     |     $       $     |     $       $
+==============================================================================+
| Titanium: {0:<67}|
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+'''


class Game:

    def __init__(self, animation: Animation, locations: list[str], player: str, titanium=0):
        self.animation = animation
        self.locations = locations
        self.player = player
        self.titanium = titanium

    def run(self) -> int:
        result = LOOP
        while result < UP:
            result = Menu(STARTED.format(self.titanium), {"ex": self.explore, "up": coming_soon,
                                                          "save": self.save, "m": self.menu}).run_once()
        return EXIT if result == EXIT else result - 1

    @staticmethod
    def menu() -> int:
        return Menu(MENU, {"back": lambda: LOOP, "main": lambda: TWO_UP,
                           "save": coming_soon, "exit": exit_}).run_once()

    def save(self) -> int:
        StateManager(self.player, self.titanium).save()
        return LOOP

    def explore(self) -> int:
        self.titanium += Explorer(self.animation, self.locations).explore()
        return LOOP


def coming_soon() -> int:
    print('Coming SOON! Thanks for playing!')
    return EXIT


def exit_() -> int:
    print('Thanks for playing, bye!')
    return EXIT
