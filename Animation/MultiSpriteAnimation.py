from Sprites.MultiSprite import MultiSprite


class MultiSpriteAnimation:
    def __init__(self, sprite: MultiSprite, on_finish_animate=None):
        self.sprite = sprite
        self.is_play = True
        self.is_finish = False
        self.is_already_callback = False
        self.frame = 0
        self.on_finish_animate = on_finish_animate

    def animate(self):
        pass

    def tick(self):
        if self.is_play:
            self.animate()
            self.frame += 1
        self.tick_callback()

    def tick_callback(self):
        if self.is_finish and not self.is_already_callback:
            self.callback()

    def callback(self):
        self.on_finish_animate(self.sprite)
        self.is_already_callback = True
