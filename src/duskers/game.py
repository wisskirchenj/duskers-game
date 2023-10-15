from duskers.menu import Menu, LOOP, UP
from duskers.play import Play, coming_soon, exit_

MAIN_MENU = '''+=======================================================================+
  ######*   ##*   ##*  #######*  ##*  ##*  #######*  ######*   #######*
  ##*  ##*  ##*   ##*  ##*       ##* ##*   ##*       ##*  ##*  ##*
  ##*  ##*  ##*   ##*  #######*  #####*    #####*    ######*   #######*
  ##*  ##*  ##*   ##*       ##*  ##* ##*   ##*       ##*  ##*       ##*
  ######*    ######*   #######*  ##*  ##*  #######*  ##*  ##*  #######*
                      (Survival ASCII Strategy Game)
+=======================================================================+

[Play]
[High] Scores
[Help]
[Exit]
'''
BEGIN = '''Are you ready to begin?
[Yes] [No] Return to Main[Menu]
'''
HIGH = '''No scores to display.
        [Back]
'''


def start() -> int:
    return Play().run()


def start_later() -> int:
    print("How about now.")
    return LOOP


def play() -> int:
    print('Enter your name:')
    name = input()
    print(f'\nGreetings, commander {name}!')
    return Menu(BEGIN, {"yes": start, "no": start_later, "menu": lambda: UP}).loop()


def high() -> int:
    return Menu(HIGH, {"back": lambda: LOOP}).run_once()


def main_menu():
    Menu(MAIN_MENU, {"play": play, "high": high, "help": coming_soon, "exit": exit_}).loop()


if __name__ == '__main__':
    main_menu()
