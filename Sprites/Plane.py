from Sprites.FlyTransport import FlyTransport

class Plane(FlyTransport):
    def __init__(self, x: int, y: int, images: list, size=[0, 0], fuel=100,  rateFuel=50, mass=10, landTime=10, takeOffTime=10):
        super().__init__(x, y, images, size, fuel, rateFuel, mass, landTime, takeOffTime)
