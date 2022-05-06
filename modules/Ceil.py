from modules.Ship import Ship
from typing import Optional


class Ceil:

    def __init__(self, size: int, number: int):
        self.is_ship: bool = False
        self.is_miss_hit: bool = False
        self.is_perfect_hit: bool = False
        self.is_touched_ceil: bool = False
        self.contains_ship: Optional[Ship] = None

    def my_draw(self) -> str:

        if self.is_ship and self.contains_ship.is_alive():
            return '▣'

        elif self.is_perfect_hit:
            return '✘'

        elif self.is_miss_hit:
            return '·'

        return '▢'


    def bot_draw(self) -> str:

        if self.is_perfect_hit:
            return '✘'

        elif self.is_miss_hit:
            return '·'

        return '▢'