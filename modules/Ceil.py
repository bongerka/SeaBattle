class Ceil:

    def __init__(self, size: int, number: int):
        self.is_ship: bool = False
        self.is_miss: bool = False
        self.is_hit: bool = False
        self.is_touched_ceil: bool = False
        self.contains_ship = None


    def get_shot(self):
        self.is_touched_ceil = True

        if self.contains_ship:
            self.is_hit = True
            return self.contains_ship;

        self.is_miss = True

        return False
        

    def draw(self, visible: bool = True) -> str:

        if self.is_ship and not self.contains_ship.is_alive():
            return '✓'

        if self.is_hit:
            return '✘'

        if self.is_miss:
            return '·'

        if visible and self.is_ship and self.contains_ship.is_alive():
            return '▣'

        return '▢'
