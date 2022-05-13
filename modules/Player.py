from modules.Field import MyField, BotField
from modules.Ship import Ship
from random import randint
from typing import List
import string


class Player:

    def __init__(self, size: int):
        self._size: int = size
        self.ships: List[Ship] = []
        self.field: list = []
        self.LETTERS: str = string.ascii_uppercase[:size]

    def get_field(self) -> list:
        return self.field._field

    def is_lose(self) -> bool:
        return not any(ship.hp for ship in self.ships)


class MyPlayer(Player):

    def __init__(self, size: int):
        super().__init__(size)
        self.field = MyField(size)
        self.ships: List[Ship] = self.field.get_ships()

    def add_ship(self, x: int, y: int, direction: str,
                 ship_instance: Ship) -> bool:
        return self.field.get_ship(x, y, direction, ship_instance)

    def move(self) -> None:
        is_miss: bool = True

        while is_miss:
            flag: bool = True

            while flag:
                x = randint(0, self._size - 1)
                y = randint(0, self._size - 1)
                shot_ceil = y * self._size + x

                if not self.get_field()[shot_ceil].is_touched_ceil:
                    flag = False

            hit_ship: Ship = self.get_field()[shot_ceil].get_shot()

            if hit_ship:
                hit_ship.get_damage()

            else:
                is_miss = False


class BotPlayer(Player):

    def __init__(self, size: int):
        super().__init__(size)
        self.field = BotField(size)
        self.ships: List[Ship] = self.field.get_ships()

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
