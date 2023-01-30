from pygame import Surface, Rect


class Sprite:
    def __init__(self, x: int, y: int, w: int, h: int):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.coord = (x, y)
        self.show = True

    def move(self, x: int, y: int):
        self.x, self.y = x, y
        self.coord = (x, y)

    def get_rect(self):
        return Rect(self.x, self.y, self.w, self.h)

    def check_collision(self, rect: Rect) -> bool:
        if self.y < 470:
            return self.get_rect().colliderect(rect)
        return False

    def draw(self, screen: Surface):
        pass

    def update(self):
        pass
