import pygame

from Sprites.FlyTransport import FlyTransport
from const import screen_height, fps


class Plane(FlyTransport):
    @staticmethod
    def get_instance(x, y):
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
                             'Sprites/Airplane/RightStrip/Landed.png']])

    def __init__(self, x: int, y: int, images: list, size=[0, 0], fuel=100, rateFuel=50, mass=10, landTime=10,
                 takeOffTime=10):
        super().__init__(x, y, images, size, fuel, rateFuel, mass, landTime, takeOffTime)

    def _animation_landA(self, frame):
        if frame == 0:
            self.current_img = pygame.Surface((4, 4))
            self.current_img.fill('black')
            self.move(1280 - self.current_img.get_size()[0] - 80, 10)
        elif frame == fps * 2:
            self.size = [11, 7]
        elif frame == fps * 5:
            self.velocity[0] = -self.velocity[1]
        # elif frame == fps * 9:
        #     self.velocity[0] = 0.1

        if frame <= fps * 2:
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] += 0.010
            self.velocity[1] += 0.015
        elif fps * 2 < frame <= fps * 5:
            self.current_img = pygame.transform.scale(self.sprites[0][3], self.size)
            self.size[0] += 11 / 30
            self.size[1] += 7 / 30
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] += 0.037
            self.velocity[1] += 0.015
        elif fps * 5 < frame <= fps * 8:
            self.current_img = pygame.transform.scale(self.sprites[0][5], self.size)
            self.size[0] += 22 / 30
            self.size[1] += 14 / 30
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] += self.velocity[0] * 0.001
            self.velocity[1] -= self.velocity[1] * 0.005
        elif fps * 8 < frame <= fps * 12:
            self.current_img = pygame.transform.scale(self.sprites[0][5], self.size)
            self.size[0] += 22 / 30
            self.size[1] += 14 / 30
            self.x += self.velocity[0]
            self.y += self.velocity[1]

        if frame > fps * 12:
            self.lA = False
            self.frame = 0

    def _animation_landB(self, frame):
        if frame == 0:
            self.current_img = pygame.Surface((4, 4))
            self.current_img.fill('black')
            self.move(1280 - self.current_img.get_size()[0], 10)
        elif frame == fps * 2:
            self.size = [11, 7]
        elif frame == fps * 5:
            self.velocity[0] = 0.5
        elif frame == fps * 9:
            self.velocity[0] = 0.1

        if frame <= fps * 2:
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] += 0.010
            self.velocity[1] += 0.015
        elif fps * 2 < frame <= fps * 5:
            self.current_img = pygame.transform.scale(self.sprites[1][3], self.size)
            self.size[0] += 11 / 30
            self.size[1] += 7 / 30
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] += 0.037
            self.velocity[1] += 0.015
        elif fps * 5 < frame <= fps * 6:
            self.current_img = pygame.transform.scale(self.sprites[1][4], self.size)
            self.size[0] += 22 / 30
            self.size[1] += 14 / 30
            self.x -= self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[1] += 0.015
        elif fps * 6 < frame <= fps * 9:
            self.current_img = pygame.transform.scale(self.sprites[1][5], self.size)
            self.size[0] += 22 / 30
            self.size[1] += 14 / 30
            self.x -= self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[1] -= 0.02
        elif fps * 9 < frame <= fps * 12:
            self.x -= self.velocity[0]
            self.y += self.velocity[1]

        if frame > fps * 12:
            self.lB = False
            self.frame = 0

    def _animation_takeOffA(self, frame):
        if frame == 0:
            self.current_img = pygame.transform.scale(self.sprites[0][0],
                                                      (self.sprites[0][0].get_size()[0] * 0.7,
                                                       self.sprites[0][0].get_size()[1] * 0.7))
            self.sprites[0][0] = self.current_img
            self.x = 220
            self.y = screen_height - 230
            self.size = list(self.current_img.get_size())
        elif frame == fps * 12 + 2:
            self.current_img = pygame.Surface((3, 3))
            self.current_img.fill('black')

        if frame <= fps * 6:
            self.current_img = pygame.transform.scale(self.sprites[0][0], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] *= 1.01
            self.velocity[1] *= 1.01
            self.size[0] *= 0.999
            self.size[1] *= 0.999
        elif fps * 6 < frame <= fps * 8:
            self.current_img = pygame.transform.scale(self.sprites[0][0], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] *= 1.01
            self.velocity[1] *= 1.01
            self.size[0] *= 0.995
            self.size[1] *= 0.995
        elif fps * 8 < frame <= fps * 9:
            self.current_img = pygame.transform.scale(self.sprites[0][0], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] *= 1.005
            self.velocity[1] *= 1.005
            self.size[0] *= 0.990
            self.size[1] *= 0.990
        elif fps * 9 < frame <= fps * 10:
            self.current_img = pygame.transform.scale(self.sprites[0][1], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] *= 0.999
            self.velocity[1] *= 0.999
            self.size[0] *= 0.98
            self.size[1] *= 0.98
        elif fps * 10 < frame <= fps * 11:
            self.current_img = pygame.transform.scale(self.sprites[0][2], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] *= 0.99
            self.velocity[1] *= 0.95
            self.size[0] *= 0.97
            self.size[1] *= 0.97
        elif fps * 11 < frame <= fps * 12:
            self.current_img = pygame.transform.scale(self.sprites[0][2], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] *= 0.999
            self.velocity[1] *= 0.99
            self.size[0] *= 0.97
            self.size[1] *= 0.97
        elif fps * 12 < frame <= fps * 20:
            self.x += self.velocity[0]
            self.y += self.velocity[1]

    def _animation_takeOffB(self, frame):
        if frame == 0:
            self.current_img = pygame.transform.scale(self.sprites[1][0],
                                                      (self.sprites[1][0].get_size()[0] * 0.5,
                                                       self.sprites[1][0].get_size()[1] * 0.5))
            self.sprites[1][0] = self.current_img
            self.x = 610
            self.y = screen_height - 230
            self.size = list(self.current_img.get_size())
        elif frame == fps * 13 + 2:
            self.current_img = pygame.Surface((3, 3))
            self.current_img.fill('black')

        if frame <= fps * 6:
            self.current_img = pygame.transform.scale(self.sprites[1][0], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] *= 1.01
            self.velocity[1] *= 1.01
            self.size[0] *= 0.998
            self.size[1] *= 0.998
        elif fps * 6 < frame <= fps * 7:
            self.current_img = pygame.transform.scale(self.sprites[1][0], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] *= 1.01
            self.velocity[1] *= 1.01
            self.size[0] *= 0.993
            self.size[1] *= 0.993
        elif fps * 7 < frame <= fps * 8:
            self.current_img = pygame.transform.scale(self.sprites[1][0], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] *= 1.005
            self.velocity[1] *= 1.005
            self.size[0] *= 0.99
            self.size[1] *= 0.99
        elif fps * 8 < frame <= fps * 9:
            self.current_img = pygame.transform.scale(self.sprites[1][0], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] *= 0.98
            self.size[0] *= 0.99
            self.size[1] *= 0.99
        elif fps * 9 < frame <= fps * 10:
            self.current_img = pygame.transform.scale(self.sprites[1][1], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.size[0] *= 0.99
            self.size[1] *= 0.99
        elif fps * 10 < frame <= fps * 11:
            self.current_img = pygame.transform.scale(self.sprites[1][1], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.size[0] *= 0.99
            self.size[1] *= 0.99
        elif fps * 11 < frame <= fps * 12:
            self.current_img = pygame.transform.scale(self.sprites[1][1], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] *= 1.05
            self.velocity[1] *= 0.97
            self.size[0] *= 0.97
            self.size[1] *= 0.97
        elif fps * 12 < frame <= fps * 13:
            self.current_img = pygame.transform.scale(self.sprites[1][2], self.size)
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[1] *= 0.97
            self.size[0] *= 0.99
            self.size[1] *= 0.99
        elif fps * 13 < frame <= fps * 20:
            self.x += self.velocity[0]
            self.y += self.velocity[1]

    def landing(self, strip: chr):
        if strip == 'A':
            self.lA = True
        elif strip == 'B':
            self.lB = True
        self.velocity = [-5, 0]

    def takeOff(self, strip: chr):
        if strip == 'A':
            self.tA = True
            self.velocity = [0.25, -0.18]
        elif strip == 'B':
            self.tB = True
            self.velocity = [0.1, -0.18]
