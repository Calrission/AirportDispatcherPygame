from pygame import Surface


class Sprite():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.coord = (x, y)

    def move(self, x: int, y: int):
        self.x, self.y = x, y
        self.coord = (x, y)

    def draw(self, screen: Surface):
        pass

    def update(self):
        pass
