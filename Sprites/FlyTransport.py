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
        self.is_finish = False
        self.velocity = [0, 0]
        self.ID = ID

    def landing(self):
        self.status = StatusFlyTransport.FLY

    def takeOff(self):
        self.status = StatusFlyTransport.GROUND

    def update(self):
        if self.animation is not None and not self.is_finish:
            if self.animation.is_finish:
                self.is_finish = True
            elif self.animation.is_play:
                self.animation.tick()

    def addRound(self):
        pass

    def fall(self):
        self.status = StatusFlyTransport.DEAD

    def fail_take_off(self):
        self.status = StatusFlyTransport.DEAD
