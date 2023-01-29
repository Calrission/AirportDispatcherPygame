from pygame import Surface, Rect


class Sprite:
    def __init__(self, x: int, y: int, w: int, h: int):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = Rect(x, y, w, h)
        self.coord = (x, y)
        self.show = True

    def move(self, x: int, y: int):
        self.x, self.y = x, y
        self.coord = (x, y)

    def check_collision(self, rect: Rect) -> bool:
        return self.rect.colliderect(rect)

    def draw(self, screen: Surface):
        pass

    def update(self):
        pass
