import random

from duskers.animation import Animation

EXPLORED = '''{0} explored successfully, with no damage taken.
Acquired {1} lumps of titanium'''


class Explorer:

    def __init__(self, animation: Animation, locations: list[str]):
        self.animation = animation
        self.locations = locations
        self.locations_to_explore: list[tuple[str, int]] = []

    def explore(self) -> int:
        self.locations_to_explore.clear()
        locations_amount = random.randint(1, 9)
        self.do_new_search()
        return self.explore_loop(locations_amount)

    def explore_loop(self, locations_amount: int) -> int:
        searched_amount = 1
        while True:
            choice = input('Your command: ').lower()
            if choice.isnumeric() and 0 < int(choice) <= searched_amount:
                return self.deploy(choice)
            elif choice == 's':
                searched_amount = self.search(locations_amount, searched_amount)
            elif choice == 'back':
                break
            else:
                print('Invalid input')
        return 0

    def search(self, locations_amount, searched_amount):
        if searched_amount < locations_amount:
            self.do_new_search()
            searched_amount += 1
        else:
            print('Nothing more in sight.\n       [Back]\n')
        return searched_amount

    def do_new_search(self):
        self.animation.animate_text("Searching")
        self.locations_to_explore.append((random.choice(self.locations), random.randint(10, 100)))
        for (i, tup) in enumerate(self.locations_to_explore):
            print(f'[{i + 1}] {tup[0]}')
        print('\n[S] to continue searching\n')

    def deploy(self, choice: str):
        location, titanium = self.locations_to_explore[int(choice) - 1]
        self.animation.animate_text("Deploying robots")
        print(EXPLORED.format(location, titanium))
        return titanium
