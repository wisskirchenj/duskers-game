from typing import Callable


class Menu:
    def __init__(self, text: str, menu_actions: dict[str, Callable],
                 invalid_message: str = 'Invalid input\n', case_sensitive: bool = False,
                 leave_menu_key: str = None):
        self.text = text
        self.menu_actions = menu_actions
        self.invalid_message = invalid_message
        self.case_sensitive = case_sensitive
        self.leave_menu_key = leave_menu_key

    def run_once(self) -> str:
        choice = self.get_menu_input()
        while choice not in self.menu_actions:
            print(self.invalid_message)
            choice = self.get_menu_input()
        self.menu_actions[choice]()
        return choice

    def loop(self):
        choice = self.run_once()
        while choice != self.leave_menu_key:
            choice = self.run_once()

    def get_menu_input(self):
        print(self.text)
        user_input = input()
        return user_input if self.case_sensitive else user_input.lower()
