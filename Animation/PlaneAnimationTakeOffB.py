import pygame

from Animation.PlaneAnimation import PlaneAnimation
from const import screen_height, fps


class PlaneAnimationTakeOffB(PlaneAnimation):
    def __init__(self, plane):
        super().__init__(plane)
        self.velocity = [0.1, -0.18]

    def animate(self):
        if self.frame == 0:
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[1][0],
                                                      (self.sprite.sprites[1][0].get_size()[0] * 0.5,
                                                       self.sprite.sprites[1][0].get_size()[1] * 0.5))
            self.sprite.sprites[1][0] = self.sprite.current_img
            self.sprite.x = 610
            self.sprite.y = screen_height - 230
            self.sprite.size = list(self.sprite.current_img.get_size())
        elif self.frame == fps * 13 + 2:
            self.sprite.current_img = pygame.Surface((3, 3))
            self.sprite.current_img.fill('black')

        if self.frame <= fps * 6:
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[1][0], self.sprite.size)
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.velocity[0] *= 1.01
            self.velocity[1] *= 1.01
            self.sprite.size[0] *= 0.998
            self.sprite.size[1] *= 0.998
        elif fps * 6 < self.frame <= fps * 7:
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[1][0], self.sprite.size)
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.velocity[0] *= 1.01
            self.velocity[1] *= 1.01
            self.sprite.size[0] *= 0.993
            self.sprite.size[1] *= 0.993
        elif fps * 7 < self.frame <= fps * 8:
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[1][0], self.sprite.size)
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.velocity[0] *= 1.005
            self.velocity[1] *= 1.005
            self.sprite.size[0] *= 0.99
            self.sprite.size[1] *= 0.99
        elif fps * 8 < self.frame <= fps * 9:
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[1][0], self.sprite.size)
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.velocity[0] *= 0.98
            self.sprite.size[0] *= 0.99
            self.sprite.size[1] *= 0.99
        elif fps * 9 < self.frame <= fps * 10:
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[1][1], self.sprite.size)
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.sprite.size[0] *= 0.99
            self.sprite.size[1] *= 0.99
        elif fps * 10 < self.frame <= fps * 11:
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[1][1], self.sprite.size)
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.sprite.size[0] *= 0.99
            self.sprite.size[1] *= 0.99
        elif fps * 11 < self.frame <= fps * 12:
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[1][1], self.sprite.size)
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.velocity[0] *= 1.05
            self.velocity[1] *= 0.97
            self.sprite.size[0] *= 0.97
            self.sprite.size[1] *= 0.97
        elif fps * 12 < self.frame <= fps * 13:
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[1][2], self.sprite.size)
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.velocity[1] *= 0.97
            self.sprite.size[0] *= 0.99
            self.sprite.size[1] *= 0.99
        elif fps * 13 < self.frame <= fps * 20:
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]

        if self.frame > fps * 20:
            self.is_play = False
            self.is_finish = True
            self.frame = 0
