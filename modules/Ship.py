class Ship:

    def __init__(self, size: int):
        self._size: int = size
        self._hp: int = size

    def set_coords(self, x: int, y: int, direction: str) -> None:
        self._x = x
        self._y = y
        self._direction = direction

    def is_alive(self) -> bool:
        return self._hp

    def get_damage(self) -> None:
        self._hp -= 1

    def size(self) -> int:
        return self._size
