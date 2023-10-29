import jsonpickle
import os
from datetime import datetime

from duskers.state import State

SAVE_PATH = "save_file.json"
SAVED_SUCCESS = '''                        |==============================|
                        |    GAME SAVED SUCCESSFULLY   |
                        |==============================|'''
LOAD_SUCCESS = '''                        |==============================|
                        |    GAME LOADED SUCCESSFULLY  |
                        |==============================|'''
SLOT_SELECT = '''   Select save slot:
    [1] {0}
    [2] {1}
    [3] {2}

Your command:'''


def load_states() -> dict[str, State]:
    if os.path.isfile(SAVE_PATH):
        with open(SAVE_PATH, 'r') as file:
            return jsonpickle.decode(file.read())
    else:
        return {}


class StateManager:

    def __init__(self, player: str = '', titanium: int = 0, robots: int = 3, upgrades: str = ''):
        self.player = player
        self.titanium = titanium
        self.robots = robots
        self.upgrades = upgrades
        self.states = load_states()

    def save(self):
        slots_prompt = self.get_slot_prompt()
        while True:
            choice = input(slots_prompt).lower()
            if choice.isnumeric() and 1 <= int(choice) <= 3:
                self.states[choice] = State(self.player, self.titanium, self.robots, self.upgrades,
                                            datetime.now().isoformat(sep=' ', timespec='minutes'))
                self.save_to_file()
                break
            elif choice == 'back':
                break
            else:
                print('Invalid input')

    def save_to_file(self):
        with open(SAVE_PATH, 'w') as file:
            file.write(jsonpickle.encode(self.states))
        print(SAVED_SUCCESS)

    def get_slot_prompt(self):
        return SLOT_SELECT.format(*[self.states.get(str(i), 'empty') for i in range(1, 4)])

    def load(self) -> State | None:
        slots_prompt = self.get_slot_prompt()
        while True:
            choice = input(slots_prompt).lower()
            if choice.isnumeric() and 1 <= int(choice) <= 3:
                if choice in self.states:
                    print(LOAD_SUCCESS)
                    return self.states[choice]
                print('Empty slot!')
            elif choice == 'back':
                break
            else:
                print('Invalid input')
        return None
