import random
import string
from typing import List
from modules.Ship import Ship
from modules.Ceil import Ceil


class Field:

    LETTERS: str = string.ascii_uppercase

    def __init__(self, size: int):
        self._size: int = size
        self._field: List[Ceil] = [Ceil(size, i) for i in range(size ** 2)]
        self.LETTERS = self.LETTERS[:size]
        self._ships = [Ship(1) for i in range(4)] + \
                        [Ship(2) for i in range(3)] + \
                        [Ship(3) for i in range(2)] + \
                        [Ship(4)]
        self.ships_sizes = self._ships.copy()


    def is_ceil_for_new_ship(self, ceil_index: int) -> bool:

        flags: int = 0

        if 0 <= ceil_index < self._size ** 2 and not self._field[ceil_index].is_ship:
            flags += 1
        else:
            return False

        # right
        if ((ceil_index % self._size < self._size - 1 and
             not self._field[ceil_index + 1].is_ship) or
            (ceil_index % self._size == self._size - 1)
            ):
            flags += 1

        # up-right
        if ((ceil_index % self._size < self._size - 1 and
             ceil_index // self._size > 0 and
             not self._field[ceil_index + 1 - self._size].is_ship) or
            (ceil_index % self._size == self._size - 1 or
                     ceil_index // self._size == 0)
            ):
            flags += 1

        # down-right
        if ((ceil_index % self._size < self._size - 1 and
             ceil_index // self._size < self._size - 1 and
             not self._field[ceil_index + 1 + self._size].is_ship) or
            (ceil_index % self._size == self._size - 1 or
                     ceil_index // self._size == self._size - 1)
            ):
            flags += 1

        # left
        if ((ceil_index % self._size > 0 and
             not self._field[ceil_index - 1].is_ship) or
            (ceil_index % self._size == 0)
            ):
            flags += 1

        # up-left
        if ((ceil_index % self._size > 0 and
             ceil_index // self._size > 0 and
             not self._field[ceil_index - 1 - self._size].is_ship) or
            (ceil_index % self._size == 0 or
                     ceil_index // self._size == 0)
            ):
            flags += 1

        # down-left
        if ((ceil_index % self._size > 0 and
             ceil_index // self._size < self._size - 1 and
             not self._field[ceil_index - 1 + self._size].is_ship) or
            (ceil_index % self._size == 0 or
                     ceil_index // self._size == self._size - 1)
            ):
            flags += 1

        # up
        if ((ceil_index // self._size > 0 and
             not self._field[ceil_index - self._size].is_ship) or
            (ceil_index // self._size == 0)
            ):
            flags += 1

        # down
        if ((ceil_index // self._size < self._size - 1 and
             not self._field[ceil_index + self._size].is_ship) or
            (ceil_index // self._size == self._size - 1)
            ):
            flags += 1

        return flags == 9


    def get_ships(self) -> List[Ship]:
        return self._ships
        

    def get_ship(self, x: int, y: int, direction: str,
                 ship_instance: Ship) -> bool:
        if (1 <= x <= self._size and
            1 <= y <= self._size
            ):
            current_ceil = (y - 1) * self._size + x - 1
            size = ship_instance.size()

            if (direction == 'l' and
                current_ceil % self._size + 1 >= size and
                all(self.is_ceil_for_new_ship(i)
                            for i in range(current_ceil, current_ceil - size, -1))
                ):

                ship_instance.set_coords(current_ceil % self._size,
                                         current_ceil // self._size,
                                         direction)

                for i in range(size):
                    self._field[current_ceil].contains_ship = ship_instance
                    self._field[current_ceil].is_ship = True
                    current_ceil -= 1

                return True

            if (direction == 'r' and
                self._size - current_ceil % self._size >= size and
                all(self.is_ceil_for_new_ship(i)
                            for i in range(current_ceil, current_ceil + size))
                ):
                ship_instance.set_coords(current_ceil % self._size,
                                         current_ceil // self._size,
                                         direction)

                for i in range(size):
                    self._field[current_ceil].contains_ship = ship_instance
                    self._field[current_ceil].is_ship = True
                    current_ceil += 1

                return True

            if (direction == 'u' and
                current_ceil // self._size + 1 >= size and
                all(self.is_ceil_for_new_ship(i)
                    for i in range(current_ceil, current_ceil - self._size * size, -self._size))
                ):
                ship_instance.set_coords(current_ceil % self._size,
                                         current_ceil // self._size,
                                         direction)

                for i in range(size):
                    self._field[current_ceil].contains_ship = ship_instance
                    self._field[current_ceil].is_ship = True
                    current_ceil -= self._size

                return True

            if (direction == 'd' and
                self._size - current_ceil // self._size >= size and
                all(self.is_ceil_for_new_ship(i)
                    for i in range(current_ceil, current_ceil + self._size * size, self._size))
                ):
                ship_instance.set_coords(current_ceil % self._size,
                                         current_ceil // self._size,
                                         direction)

                for i in range(size):
                    self._field[current_ceil].contains_ship = ship_instance
                    self._field[current_ceil].is_ship = True
                    current_ceil += self._size

                return True

        return False
