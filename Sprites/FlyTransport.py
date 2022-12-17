import pygame.transform
from Sprites.Transport import Transport
from const import fps

class FlyTransport(Transport):
    def __init__(self, x: int, y: int, images: list, size=[0, 0], fuel=100,  rateFuel=50, mass=10, landTime=10, takeOffTime=10):
        super().__init__(x, y, images, size, fuel, rateFuel, mass)
        self.landTime = landTime
        self.takeOffTime = takeOffTime
        self.frame = 0
        self.A = self.B = False
        self.velocity = [0, 0]

    def landing(self, strip: chr):
        if strip == 'A':
            self.A = True
            self.velocity = [-5, 0]
        elif strip == 'B':
            self.B = True

    def update(self):
        if self.A:
            self._animation_landA(self.frame)
            self.frame += 1
        elif self.B:
            self._animation_landB(self.frame)
            self.frame += 1


    def takeOff(self):
        pass

    def addRound(self):
        pass

    def _animation_landA(self, frame):

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
            self.current_img = pygame.transform.scale(self.sprites[0], self.size)
            self.size[0] += 11 / 30
            self.size[1] += 7 / 30
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[0] += 0.037
            self.velocity[1] += 0.015
        elif fps * 5 < frame <= fps * 6:
            self.current_img = pygame.transform.scale(self.sprites[2], self.size)
            self.size[0] += 22 / 30
            self.size[1] += 14 / 30
            self.x -= self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[1] += 0.015
        elif fps * 6 < frame <= fps * 9:
            self.current_img = pygame.transform.scale(self.sprites[2], self.size)
            self.size[0] += 22 / 30
            self.size[1] += 14 / 30
            self.x -= self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[1] -= 0.02
        elif fps * 9 < frame <= fps * 12:
            self.x -= self.velocity[0]
            self.y += self.velocity[1]





        # if frame <= fps:
        #     self.x -= 6
        #     self.y += 0.5
        # elif fps < frame <= fps * 2:
        #     self.size[0] += 11 / 30
        #     self.size[1] += 7 / 30
        #     self.current_img = pygame.transform.scale(self.sprites[0], self.size)
        #     self.x -= 5
        #     self.y += 1
        # elif fps * 2 < frame <= fps * 3:
        #     self.size[0] += 22 / 30
        #     self.size[1] += 14 / 30
        #     self.current_img = pygame.transform.scale(self.sprites[1], self.size)
        #     self.x -= 5
        #     self.y += 2
        # elif fps * 3 < frame <= fps * 4:
        #     self.size[0] += 30 / 30
        #     self.size[1] += 22 / 30
        #     self.current_img = pygame.transform.scale(self.sprites[1], self.size)
        #     self.x -= 2
        #     self.y += 2
        # elif fps * 4 < frame <= fps * 5:
        #     self.size[0] += 30 / 30
        #     self.size[1] += 22 / 30
        #     self.current_img = pygame.transform.scale(self.sprites[2], self.size)
        #     self.x -= 0.5
        #     self.y += 2
        # elif fps * 5 < frame <= fps * 8:
        #     self.x -= 0.2
        #     self.y += 2

        if frame >= fps * 100:
            self.A = False
            self.frame = 0




    def _animation_landB(self, frame):
        pass