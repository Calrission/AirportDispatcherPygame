from Sprites.MultiSprite import MultiSprite

class Transport(MultiSprite):
    def __init__(self, x: int, y: int, images: list, fuel = 100,  rateFuel = 50, mass = 10):
        super().__init__(x, y, images)
        self.fuel = fuel
        self.rateFuel = rateFuel
        self.mass = mass