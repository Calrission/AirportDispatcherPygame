import enum

from Animation.MultiSpriteAnimation import MultiSpriteAnimation
from Sprites.Transport import Transport


class StatusFlyTransport(enum.Enum):
    FLY = 0
    GROUND = 1
    DEAD = 2


class FlyTransport(Transport):
    def __init__(self, x: int, y: int, images: list, ID: str, status: StatusFlyTransport, size=[0, 0], fuel=100,
                 rateFuel=50, mass=10, landTime=10,
                 takeOffTime=10):
        super().__init__(x, y, images, size, fuel, rateFuel, mass)
        self.status = status
        self.landTime = landTime
        self.takeOffTime = takeOffTime
        self.animation: MultiSpriteAnimation = None
        self.is_already_animate = False
        self.velocity = [0, 0]
        self.ID = ID

    def landing(self):
        self.status = StatusFlyTransport.FLY

    def takeOff(self):
        self.status = StatusFlyTransport.GROUND

    def update(self):
        if self.animation is not None and self.animation.is_play:
            if not self.is_already_animate:
                self.is_already_animate = True
            self.animation.tick()
        else:
            self.animation = None

    def addRound(self):
        pass

    def fall(self):
        self.status = StatusFlyTransport.DEAD
