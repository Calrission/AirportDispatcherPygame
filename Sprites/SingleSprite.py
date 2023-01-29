from Sprites.Sprite import Sprite


# Этот класс нам вообще нах нужен ?
class SingleSprite(Sprite):
    def __init__(self, x: int, y: int, img: str):
        super().__init__(x, y, 0, 0)
        self.img = img
