import os
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
