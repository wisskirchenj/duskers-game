from typing import Callable

LOOP = 0
UP = 1
TWO_UP = 2
EXIT = 3
PROMPT = 'Your command:'


class Menu:
    def __init__(self, text: str, menu_actions: dict[str, Callable[[], int]], invalid_message: str = 'Invalid input\n',
                 case_sensitive: bool = False):
        self.text = text
        self.menu_actions = menu_actions
        self.invalid_message = invalid_message
        self.case_sensitive = case_sensitive

    def run_once(self) -> int:
        print(self.text)
        choice = self.get_menu_input()
        while choice not in self.menu_actions:
            print(self.invalid_message)
            choice = self.get_menu_input()
        return self.menu_actions[choice]()

    def loop(self) -> int:
        status = self.run_once()
        while status == LOOP:
            status = self.run_once()
        return EXIT if status == EXIT else status - 1

    def get_menu_input(self):
        print(PROMPT)
        user_input = input()
        return user_input if self.case_sensitive else user_input.lower()
