from Animation.MultiSpriteAnimation import MultiSpriteAnimation


class PlaneAnimation(MultiSpriteAnimation):
    def __init__(self, plane, on_finish_animate=None):
        super().__init__(plane)
        self.velocity = [0.0, 0.0]
        self.on_finish_animate = on_finish_animate
