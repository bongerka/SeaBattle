import string
import os
from sys import platform
from typing import Optional
from modules.Player import MyPlayer, BotPlayer


def clear() -> None:
    if platform == "linux" or platform == "linux2":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")


class Game:

    def __init__(self, size: int, first_player: str):
        self.LETTERS: str = string.ascii_uppercase[:size]
        self._size: int = size
        self.myPlayer = MyPlayer(size)
        self.botPlayer = BotPlayer(size)

    def print_tables(self) -> None:
        CENTER: int = self._size * 3
        clear()
        print('SEA BATTLE'.center(CENTER * 2))

        print('MY TABLE'.center(CENTER) + 'OPPONENT'.center(CENTER))

        print(" ".join(self.LETTERS).rjust(int(self._size * 2.5)) +
                " ".join(self.LETTERS).rjust(int(self._size * 3)))

        for i in range(0, self._size ** 2, self._size):
            print((f"{i // self._size + 1} " + 
                " ".join(i.my_draw() 
                    for i in self.myPlayer.get_field()[i:i+self._size])).rjust(int(self._size * 2.5)) +
                (f"{i // self._size + 1} " + 
                " ".join(i.bot_draw() 
                    for i in self.botPlayer.get_field()[i:i+self._size])).rjust(int(self._size * 3)))

        print()

    def get_coords(self) -> None:
        flag: bool = True
        i = 0

        while(i != len(self.myPlayer.ships) - 1):
            self.print_tables()
            print("Enter your coordinates\nExample: rD5\nr-right\nu-up\nd-down\nl-left\nD5 - start position\n*****************")

            if not flag:
                print("wrong_position for ship. Try again")

            try:
                coords = input(f'{self.myPlayer.ships[i].size()}-deck ship: ')

                flag = self.myPlayer.add_ship(self.LETTERS.index(coords[1]) + 1,
                                                int(coords[2]),
                                                coords[0],
                                                self.myPlayer.ships[i])
                if not flag:
                    i -= 1

            except:
                i -= 1
                flag = False
                
            i += 1


    def is_continue(self) -> bool:
        return all((self.myPlayer.count_of_ships,
                   self.botPlayer.count_of_ships))

    def move(self, step: str) -> bool:
        if (1 <= x <= self._size) and (y in LETTERS):
            self._players[is_human].get_hit(x, y)
            return True

        return False
