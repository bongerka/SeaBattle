from modules.Field import MyField, BotField
from modules.Ship import Ship


class Player:

    def __init__(self, size: int):
        self._size: int = size
        self.count_of_ships: int = 10
        self.ships: List[Ship] = getattr(MyField, "_ships")
        self.field: list = []

    def get_field(self) -> list:
        return self.field._field


class MyPlayer(Player):

    def __init__(self, size: int):
        super().__init__(size)
        self.field = MyField(size)

    def move(self, x: int, y: int):
        pass

    def add_ship(self, x: int, y: int, direction: str,
                 ship_instance: Ship) -> bool:
        return self.field.get_ship(x, y, direction, ship_instance)


class BotPlayer(Player):

    def __init__(self, size: int):
        super().__init__(size)
        self.field = BotField(size)

    def move(self, x: int, y: int):
        pass
