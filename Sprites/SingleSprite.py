from Sprites.Sprite import Sprite


class SingleSprite(Sprite):
    def __init__(self, x: int, y: int, img: str):
        super().__init__(x, y)
        self.img = img
