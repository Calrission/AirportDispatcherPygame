from Animation.MultiSpriteAnimation import MultiSpriteAnimation
from Sprites.Transport import Transport


class FlyTransport(Transport):
    def __init__(self, x: int, y: int, images: list, size=[0, 0], fuel=100, rateFuel=50, mass=10, landTime=10,
                 takeOffTime=10):
        super().__init__(x, y, images, size, fuel, rateFuel, mass)
        self.landTime = landTime
        self.takeOffTime = takeOffTime
        self.animation: MultiSpriteAnimation = None
        self.frame = 0
        self.lA = self.lB = self.tA = self.tB = False
        self.velocity = [0, 0]

    def landing(self, strip: chr):
        pass

    def takeOff(self, strip: chr):
        pass

    def update(self):
        if self.animation is not None:
            self.animation.tick()

    def addRound(self):
        pass
