import argparse
import random
from argparse import ArgumentParser

from duskers.animation import Animation
from duskers.menu import Menu, LOOP, UP, EXIT
from duskers.game import Game, exit_
from duskers.score_manager import ScoreManager
from duskers.state_manager import StateManager

MAIN_MENU = '''+=======================================================================+
  ######*   ##*   ##*  #######*  ##*  ##*  #######*  ######*   #######*
  ##*  ##*  ##*   ##*  ##*       ##* ##*   ##*       ##*  ##*  ##*
  ##*  ##*  ##*   ##*  #######*  #####*    #####*    ######*   #######*
  ##*  ##*  ##*   ##*       ##*  ##* ##*   ##*       ##*  ##*       ##*
  ######*    ######*   #######*  ##*  ##*  #######*  ##*  ##*  #######*
                      (Survival ASCII Strategy Game)
+=======================================================================+

[New]  Game
[Load] Game
[High] Scores
[Help]
[Exit]
'''
BEGIN = '''Are you ready to begin?
[Yes] [No] Return to Main[Menu]
'''
HIGH = '''
        [Back]
'''


class GameControl:

    def __init__(self):
        args = self.parse_commandline_arguments()
        random.seed(args.seed)
        self.animation = Animation(args.min, args.max)
        self.locations = args.locations.replace('_', ' ').split(',')
        self.player = None

    @staticmethod
    def parse_commandline_arguments() -> argparse.Namespace:
        parser = ArgumentParser(description='Duskers game')
        parser.add_argument('seed', help='random seed', nargs='?', default=None)
        parser.add_argument('min', help='lower limit for animation duration', nargs='?', type=int, default=0)
        parser.add_argument('max', help='upper limit for animation duration', nargs='?', type=int, default=0)
        parser.add_argument('locations', help='locations to search for titanium', nargs='?',
                            default='Nuclear_power_plant_wreckage,Old_beach_bar')
        return parser.parse_args()

    def start(self) -> int:
        return Game(self.animation, self.locations, self.player).run()

    @staticmethod
    def start_later() -> int:
        print("How about now.")
        return LOOP

    def new_game(self) -> int:
        self.player = input('Enter your name: ')
        print(f'\nGreetings, commander {self.player}!')
        return Menu(BEGIN, {"yes": self.start, "no": self.start_later, "menu": lambda: UP}).loop()

    def load_game(self) -> int:
        state = StateManager().load()
        if state:
            self.player = state.player
            print(f'Welcome back, commander {self.player}!')
            return EXIT if Game(self.animation, self.locations, self.player, state.titanium, state.robots,
                                state.upgrades).run() == EXIT else LOOP
        return LOOP

    @staticmethod
    def high() -> int:
        ScoreManager().show_scores()
        return Menu(HIGH, {"back": lambda: LOOP}).run_once()

    @staticmethod
    def help() -> int:
        print("This is Dusker's game. The menu is self-explanatory. "
              "Explore is used to search for titanium our currency."
              "\nWith upgrade you can buy more insight on found titanium and encounter probabilities.")
        return LOOP

    def main_menu(self):
        Menu(MAIN_MENU, {"new": self.new_game, "load": self.load_game, "high": self.high,
                         "help": self.help, "exit": exit_}).loop()


if __name__ == '__main__':
    GameControl().main_menu()
