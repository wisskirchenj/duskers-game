from time import monotonic_ns
from typing import Generator


class PseudoRandom:

    def __init__(self, min_: int, max_: int):
        self.random = self.random_generator(min_, max_)

    def get_next(self) -> int:
        return next(self.random)

    @staticmethod
    def random_generator(min_: int, max_: int) -> Generator:
        diff = max_ - min_ + 1
        while True:
            yield min_ + monotonic_ns() // 10 % diff
