import string
from typing import Optional
from modules.Player import MyPlayer, BotPlayer
from modules.Interface import Interface, clear


class Game:

    interface = Interface()

    def __init__(self, size: int, first_player: str):
        self.LETTERS: str = string.ascii_uppercase[:size]
        self._size: int = size
        self.myPlayer = MyPlayer(size)
        self.botPlayer = BotPlayer(size)


    def print_tables(self) -> None:
        CENTER: int = self._size * 3
        clear()
        self.interface.my_print('SEA BATTLE'.center(CENTER * 2))

        self.interface.my_print('MY TABLE'.center(CENTER) + 'OPPONENT'.center(CENTER))

        self.interface.my_print(" ".join(self.LETTERS).rjust(int(self._size * 2.5)) +
                " ".join(self.LETTERS).rjust(int(self._size * 3)))

        for i in range(0, self._size ** 2, self._size):
            self.interface.my_print((f"{i // self._size + 1} " + 
                " ".join(i.my_draw() 
                    for i in self.myPlayer.get_field()[i:i+self._size])).rjust(int(self._size * 2.5)) +
                (f"{i // self._size + 1} " + 
                " ".join(i.bot_draw() 
                    for i in self.botPlayer.get_field()[i:i+self._size])).rjust(int(self._size * 3)))

        self.interface.my_print()


    def get_coords(self) -> None:
        flag: bool = True
        i = len(self.myPlayer.ships) - 1

        while(i >= 0):

            self.print_tables()

            self.interface.my_print("Enter your coordinates\nExample: rD5\n" + 
                "r-right\nu-up\nd-down\nl-left\nD5 - start position\n*****************")

            if not flag:
                self.interface.my_print("wrong position for ship. Try again")

            try:
                coords = self.interface.my_input(f'{self.myPlayer.ships[i].size()}-deck ship: ')

                flag = self.myPlayer.add_ship(self.LETTERS.index(coords[1]) + 1,
                                                int(coords[2:]),
                                                coords[0],
                                                self.myPlayer.ships[i])
                if not flag:
                    i += 1

            except:
                i += 1
                flag = False
                
            i -= 1


    def set_shots(self) -> None:

        while self._is_continue():
            self.print_tables()
            self.interface.my_print("*" * 40)

            new_shot = self.interface.my_input("Enter coordinate you want to shot: ")
            flags: bool = self.botPlayer.move(new_shot)

            if not flags[0] or flags[1]:
                continue

            self.myPlayer.move()


    def winner(self) -> None:
        self.print_tables()

        if self.myPlayer.is_lose():
            self.interface.my_print("\nGAME IS OVER\nOPPONENT IS WINNER")

        elif self.botPlayer.is_lose():
            self.interface.my_print("\nGAME IS OVER\nYOU ARE WINNER")


    def _is_continue(self) -> bool:
        return not any((self.myPlayer.is_lose(),
                        self.botPlayer.is_lose()))
