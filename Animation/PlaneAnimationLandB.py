import pygame

from Animation.PlaneAnimation import PlaneAnimation
from const import fps


class PlaneAnimationLandB(PlaneAnimation):
    def __init__(self, plane):
        super().__init__(plane)
        self.velocity = [-5, 0]

    def animate(self):
        if self.frame == 0:
            self.sprite.current_img = pygame.Surface((4, 4))
            self.sprite.current_img.fill('black')
            self.sprite.move(1280 - self.sprite.current_img.get_size()[0], 10)
        elif self.frame == fps * 2:
            self.sprite.size = [11, 7]
        elif self.frame == fps * 5:
            self.velocity[0] = 0.5
        elif self.frame == fps * 9:
            self.velocity[0] = 0.1

        if self.frame <= fps * 2:
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.velocity[0] += 0.010
            self.velocity[1] += 0.015
        elif fps * 2 < self.frame <= fps * 5:
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[1][3], self.sprite.size)
            self.sprite.size[0] += 11 / 30
            self.sprite.size[1] += 7 / 30
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.velocity[0] += 0.037
            self.velocity[1] += 0.015
        elif fps * 5 < self.frame <= fps * 6:
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[1][4], self.sprite.size)
            self.sprite.size[0] += 22 / 30
            self.sprite.size[1] += 14 / 30
            self.sprite.x -= self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.velocity[1] += 0.015
        elif fps * 6 < self.frame <= fps * 9:
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[1][5], self.sprite.size)
            self.sprite.size[0] += 22 / 30
            self.sprite.size[1] += 14 / 30
            self.sprite.x -= self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.velocity[1] -= 0.02
        elif fps * 9 < self.frame <= fps * 12:
            self.sprite.x -= self.velocity[0]
            self.sprite.y += self.velocity[1]

        if self.frame > fps * 12:
            self.is_play = False
            self.frame = 0