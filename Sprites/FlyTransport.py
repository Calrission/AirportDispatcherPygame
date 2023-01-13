from Sprites.Transport import Transport


class FlyTransport(Transport):
    def __init__(self, x: int, y: int, images: list, size=[0, 0], fuel=100, rateFuel=50, mass=10, landTime=10,
                 takeOffTime=10):
        super().__init__(x, y, images, size, fuel, rateFuel, mass)
        self.landTime = landTime
        self.takeOffTime = takeOffTime
        self.frame = 0
        self.lA = self.lB = self.tA = self.tB = False
        self.velocity = [0, 0]

    def landing(self, strip: chr):
        pass

    def takeOff(self, strip: chr):
        pass

    def update(self):
        if self.lA:
            self._animation_landA(self.frame)
        elif self.lB:
            self._animation_landB(self.frame)
        elif self.tA:
            self._animation_takeOffA(self.frame)
        elif self.tB:
            self._animation_takeOffB(self.frame)
        self.frame += 1

    def addRound(self):
        pass

    def _animation_landA(self, frame):
        pass

    def _animation_landB(self, frame):
        pass

    def _animation_takeOffA(self, frame):
        pass

    def _animation_takeOffB(self, frame):
        pass
