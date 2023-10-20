from time import sleep

from duskers.pseudo_random import PseudoRandom


class Animation:

    def __init__(self, min_: int, max_: int):
        self.random = PseudoRandom(min_, max_)

    def animate_text(self, text: str):
        secs = self.random.get_next()
        print(text, end='')
        for _ in range(secs):
            sleep(1)
            print('.', end='')
        print()
