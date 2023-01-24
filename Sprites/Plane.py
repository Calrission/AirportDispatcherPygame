from Sprites.FlyTransport import FlyTransport


class Plane(FlyTransport):
    @staticmethod
    def get_instance(x, y, ID, **kwargs):
        return Plane(x, y, [['Sprites/Airplane/LeftStrip/TakesOff.png',
                             'Sprites/Airplane/LeftStrip/TakeOff.png',
                             'Sprites/Airplane/LeftStrip/GoAway.png',
                             'Sprites/Airplane/LeftStrip/GoIn.png',
                             'Sprites/Airplane/LeftStrip/Landing.png',
                             'Sprites/Airplane/LeftStrip/Landed.png'],
                            ['Sprites/Airplane/RightStrip/TakesOff.png',
                             'Sprites/Airplane/RightStrip/TakeOff.png',
                             'Sprites/Airplane/RightStrip/TakesOff.png',
                             'Sprites/Airplane/RightStrip/GoIn.png',
                             'Sprites/Airplane/RightStrip/Landing.png',
                             'Sprites/Airplane/RightStrip/Landed.png'],
                             ['Sprites/Boom.png']
                            ], ID, *kwargs)

    def __init__(self, x: int, y: int, images: list, ID:str, size=[0, 0], fuel=100, rateFuel=50, mass=10, landTime=10,
                 takeOffTime=10, capacity = 500):
        super().__init__(x, y, images, ID, size, fuel, rateFuel, mass, landTime, takeOffTime)
        self.capacity = capacity

