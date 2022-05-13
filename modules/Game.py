import string
from typing import Optional
from modules.Player import MyPlayer, BotPlayer
from modules.Interface import Interface


class Game:

    interface = Interface()

    def __init__(self, size: int, first_player: str):
        self.LETTERS: str = string.ascii_uppercase[:size]
        self._size: int = size
        self.myPlayer = MyPlayer(size)
        self.botPlayer = BotPlayer(size)


    def print_tables(self) -> None:

        my_ceils = [i.my_draw() for i in self.myPlayer.get_field()]
        bot_ceils = [i.bot_draw() for i in self.botPlayer.get_field()]

        self.interface.print_tables(self.LETTERS, self._size, my_ceils, bot_ceils)


    def get_coords(self) -> None:
        flag: bool = True
        i = len(self.myPlayer.ships) - 1

        while i >= 0:

            self.print_tables()
            self.interface.draw_coords(flag)

            try:
                coords = self.interface.take_coords(self.myPlayer.ships[i].size())

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

            new_shot = self.interface.take_shot()
            flags: bool = self.botPlayer.move(new_shot)

            if not flags[0] or flags[1]:
                continue

            self.myPlayer.move()


    def winner(self) -> None:
        self.print_tables()
        self.interface.draw_winner(self.myPlayer.is_lose(), self.botPlayer.is_lose())


    def _is_continue(self) -> bool:
        return not any((self.myPlayer.is_lose(),
                        self.botPlayer.is_lose()))
