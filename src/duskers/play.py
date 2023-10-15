from duskers.menu import Menu, EXIT, LOOP, TWO_UP

STARTED = '''+==============================================================================+
  $   $$$$$$$   $  |  $   $$$$$$$   $  |  $   $$$$$$$   $
  $$$$$     $$$$$  |  $$$$$     $$$$$  |  $$$$$     $$$$$
      $$$$$$$      |      $$$$$$$      |      $$$$$$$
     $$$   $$$     |     $$$   $$$     |     $$$   $$$
     $       $     |     $       $     |     $       $
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+'''

MENU = '''                          |==========================|
                          |            MENU          |
                          |                          |
                          | [Back] to game           |
                          | Return to [Main] Menu    |
                          | [Save] and exit          |
                          | [Exit] game              |
                          |==========================|'''


class Play:

    def run(self) -> int:
        return Menu(STARTED, {"ex": coming_soon, "up": coming_soon,
                              "save": coming_soon, "m": self.menu}).loop()

    def menu(self) -> int:
        return Menu(MENU, {"back": lambda: LOOP, "main": lambda: TWO_UP,
                           "save": coming_soon, "exit": exit_}).run_once()


def coming_soon() -> int:
    print('Coming SOON! Thanks for playing!')
    return EXIT


def exit_() -> int:
    print('Thanks for playing, bye!')
    return EXIT
