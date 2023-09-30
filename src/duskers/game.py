from duskers.menu import Menu

MAIN_MENU = '''[Play]
[Exit]
'''
ASCII_ART = '''+=======================================================================+
  ######*   ##*   ##*  #######*  ##*  ##*  #######*  ######*   #######*
  ##*  ##*  ##*   ##*  ##*       ##* ##*   ##*       ##*  ##*  ##*
  ##*  ##*  ##*   ##*  #######*  #####*    #####*    ######*   #######*
  ##*  ##*  ##*   ##*       ##*  ##* ##*   ##*       ##*  ##*       ##*
  ######*    ######*   #######*  ##*  ##*  #######*  ##*  ##*  #######*
                      (Survival ASCII Strategy Game)
+=======================================================================+'''
BEGIN = '''Are you ready to begin?
    [Yes] [No]
'''


def start():
    print("Great, now let's go code some more ;)")


def start_later():
    print("How about now.")
    print(BEGIN)


def play():
    print('Enter your name:')
    name = input()
    print(f'\nGreetings, commander {name}!')
    print(BEGIN)
    Menu('Your command:', {"yes": start, "no": start_later}, leave_menu_key="yes").loop()


def exit_game():
    print('Thanks for playing, bye!')


def welcome():
    print(ASCII_ART)
    print(MAIN_MENU)
    Menu('Your command:', {"play": play, "exit": exit_game}).run_once()


if __name__ == '__main__':
    welcome()
