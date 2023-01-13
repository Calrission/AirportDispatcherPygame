from Animation.MultiSpriteAnimation import MultiSpriteAnimation


class PlaneAnimation(MultiSpriteAnimation):
    def __init__(self, plane):
        super().__init__(plane)
        self.velocity = [0.0, 0.0]