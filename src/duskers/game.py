from duskers.menu import Menu, EXIT, LOOP, UP

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
STARTED = '''__________(LOG)__________________________________________________(LOG)__________
+==============================================================================+


                                 (ROBOT IMAGES)


+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+'''


def start() -> int:
    print(STARTED)
    return EXIT


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


def help_() -> int:
    print('Coming SOON! Thanks for playing!')
    return EXIT


def exit_() -> int:
    print('Thanks for playing, bye!')
    return EXIT


def main_menu():
    Menu(MAIN_MENU, {"play": play, "high": high, "help": help_, "exit": exit_}).loop()


if __name__ == '__main__':
    main_menu()
