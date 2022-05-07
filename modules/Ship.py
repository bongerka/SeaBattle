class Ship:

    def __init__(self, size: int):
        self._size: int = size
        self.hp: int = size

    def set_coords(self, x: int, y: int, direction: str) -> None:
        self.x = x
        self.y = y
        self.direction = direction


    def is_alive(self) -> bool:
        return self.hp

    def get_damage(self) -> None:
        self.hp -= 1

    def size(self) -> int:
        return self._size
