import string
from typing import Optional
from modules.Player import Player
from modules.Interface import Interface


class Game:

    interface = Interface()

    def __init__(self, size: int, first_player: str):
        self.LETTERS: str = string.ascii_uppercase[:size]
        self._size: int = size
        self.myplayer_1 = Player(size)
        self.myplayer_2 = Player(size)


    def print_tables(self, player1: bool, player2: bool) -> None:

        my_ceils = [i.draw(player1) for i in self.myplayer_1.get_field()]
        opp_ceils = [i.draw(player2) for i in self.myplayer_2.get_field()]

        self.interface.print_tables(self.LETTERS, self._size, my_ceils, opp_ceils)


    def coord(self, player: Player, player1: bool, player2: bool):
        flag: bool = True
        i = len(player.ships) - 1

        while i >= 0:

            self.print_tables(player1, player2)
            self.interface.draw_coords(flag)

            try:
                coords = self.interface.take_coords(player.ships[i].size())

                flag = player.add_ship(self.LETTERS.index(coords[1]) + 1,
                                                int(coords[2:]),
                                                coords[0],
                                                player.ships[i])
                if not flag:
                    i += 1

            except:
                i += 1
                flag = False

            i -= 1      


    def get_coords(self) -> None:
        self.coord(self.myplayer_1, True, False)
        self.coord(self.myplayer_2, False, True)


    def set_shots(self) -> None:

        while self._is_continue():

            self.print_tables(True, False)

            new_shot = self.interface.take_shot()
            flags: bool = self.myplayer_2.move(new_shot)

            if not flags[0] or flags[1]:
                continue

            self.print_tables(False, True)

            new_shot = self.interface.take_shot()
            flags: bool = self.myplayer_1.move(new_shot)



    def winner(self) -> None:
        self.print_tables(True, True)
        self.interface.draw_winner(self.myplayer_1.is_lose(), self.myplayer_2.is_lose())


    def _is_continue(self) -> bool:
        return not any((self.myplayer_1.is_lose(),
                        self.myplayer_2.is_lose()))
