from Sprites.FlyTransport import FlyTransport

class Plane(FlyTransport):
    def __init__(self, x: int, y: int, images: list, fuel=100,  rateFuel=50, mass=10, landTime=10, takeOffTime=10):
        super().__init__(x, y, images, fuel, rateFuel, mass, landTime, takeOffTime)
