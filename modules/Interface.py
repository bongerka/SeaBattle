import os
from typing import List
from sys import platform


def clear() -> None:

    if platform == "linux" or platform == "linux2":
        os.system("clear")

    elif platform == "win32":
        os.system("cls")


class Interface:

    def __init__(self):
        clear()


    def my_input(self, string: str = "") -> str:
        return input(string)


    def my_print(self, string: str = "") -> None:
        print(string)


    def print_tables(self, LETTERS: str, size: int,
                        my_ceils: List[List[str]], bot_ceils: List[List[str]]) -> None:
        CENTER: int = size * 3

        clear()
        self.my_print('SEA BATTLE'.center(CENTER * 2))
        self.my_print('ME'.center(CENTER) + 'OPPONENT'.center(CENTER))
        self.my_print(" ".join(LETTERS).rjust(int(size * 2.5)) +
                " ".join(LETTERS).rjust(int(size * 3)))

        for i in range(0, size ** 2, size):
            self.my_print((f"{i // size + 1} " +
                " ".join(my_ceils[i:i+size])).rjust(int(size * 2.5)) +
                (f"{i // size + 1} " +
                " ".join(bot_ceils[i:i+size])).rjust(int(size * 3)))

        self.my_print()


    def take_coords(self, size_ship: int) -> str:
        return self.my_input(f'{size_ship}-deck ship: ')


    def draw_coords(self, flag: bool) -> None:

        self.my_print("Enter your coordinates\nExample: rD5\n" +
                "r-right\nu-up\nd-down\nl-left\nD5 - start position\n*****************")

        if not flag:
            self.my_print("wrong position for ship. Try again")


    def take_shot(self):
        self.my_print("*" * 40)
        
        return self.my_input("Enter coordinate you want to shot: ")


    def draw_winner(self, my_win: bool, not_wins: bool):

        if my_win:
            self.my_print("\nGAME IS OVER\nOPPONENT IS WINNER")

        elif bot_wins:
            self.my_print("\nGAME IS OVER\nYOU ARE WINNER")