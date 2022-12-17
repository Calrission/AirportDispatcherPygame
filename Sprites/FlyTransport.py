from Sprites.Transport import Transport

class FlyTransport(Transport):
    def __init__(self, x: int, y: int, images: list, fuel=100,  rateFuel=50, mass=10, landTime=10, takeOffTime=10):
        super().__init__(x, y, images, fuel, rateFuel, mass)
        self.landTime = landTime
        self.takeOffTime = takeOffTime

    def landing(self, strip: chr):
        if strip == 'A':
            self._animation_landA()
        elif strip == 'B':
            self._animation_landB()


    def takeOff(self):
        pass

    def addRound(self):
        pass

    def _animation_landA(self):
        self.x = 200
        self.y = 200

    def _animation_landB(self):
        pass