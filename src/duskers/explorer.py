import random

from duskers.animation import Animation


class Explorer:

    def __init__(self, animation: Animation, locations: list[str], upgrades: str, robots: int):
        self.animation = animation
        self.locations = locations
        self.upgrades = upgrades
        self.robots = robots
        self.locations_to_explore: list[tuple[str, int, float]] = []

    def explore(self) -> (int, bool):
        self.locations_to_explore.clear()
        locations_amount = random.randint(1, 9)
        self.do_new_search()
        return self.explore_loop(locations_amount)

    def explore_loop(self, locations_amount: int) -> (int, bool):
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
        return 0, False

    def search(self, locations_amount, searched_amount):
        if searched_amount < locations_amount:
            self.do_new_search()
            searched_amount += 1
        else:
            print('Nothing more in sight.\n       [Back]\n')
        return searched_amount

    def do_new_search(self):
        self.animation.animate_text("Searching")
        location, titanium = random.choice(self.locations), random.randint(10, 100)
        encounter_rate = random.random()
        self.locations_to_explore.append((location, titanium, encounter_rate))
        for (i, tup) in enumerate(self.locations_to_explore):
            print(self.get_location_info(i, tup[:3]))
        print('\n[S] to continue searching\n')

    def deploy(self, choice: str) -> (int, bool):
        location, titanium, encounter_rate = self.locations_to_explore[int(choice) - 1]
        encounter = random.random() < encounter_rate
        self.animation.animate_text("Deploying robots")
        if encounter:
            if self.robots == 1:
                return 0, True
            print('Enemy encounter')
        print(f'{location} explored successfully,', '1 robot lost..' if encounter else 'with no damage taken.')
        print(f'Acquired {titanium} lumps of titanium')
        return titanium, encounter

    def get_location_info(self, i: int, tup: tuple[str, int, float]) -> str:
        location, titanium, encounter_rate = tup
        location_info = f'[{i + 1}] {location}'
        if 'T' in self.upgrades:
            location_info += f' Titanium: {titanium}'
        if 'E' in self.upgrades:
            location_info += f' Encounter rate: {round(encounter_rate * 100)}%'
        return location_info
