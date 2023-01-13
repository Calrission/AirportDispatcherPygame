from Sprites.MultiSprite import MultiSprite
from const import fps


class MultiSpriteAnimation:
    def __init__(self, sprite: MultiSprite):
        self.sprite = sprite
        self.is_play = True
        self.frame = 0

    def animate(self):
        pass

    def tick(self):
        if self.is_play:
            self.animate()
            self.frame += 1
