from modules.Field import Field
from random import randint
from typing import List
import string


class Player:

    def __init__(self, size: int):
        self._size: int = size
        self.ships: List[Ship] = []
        self.field: list = []
        self.LETTERS: str = string.ascii_uppercase[:size]
        self.field = Field(size)
        self.ships: list = self.field.get_ships()

    def get_field(self) -> list:
        return self.field._field

    def is_lose(self) -> bool:
        return not any(ship.hp for ship in self.ships)


    def add_ship(self, x: int, y: int, direction: str,
                 ship_instance) -> bool:
        return self.field.get_ship(x, y, direction, ship_instance)

    def move(self, hit: str):
        try:
            x = self.LETTERS.index(hit[0])
            y = int(hit[1:]) - 1
            shot_ceil = y * self._size + x

            if (0 <= y < self._size and 
                0 <= x < self._size):
                hit_ship: Ship = self.get_field()[shot_ceil].get_shot()

                if hit_ship:
                    hit_ship.get_damage()
                    return True, True

                return True, False

            return False, False

        except:
            return False, False
