import pygame

from Animation.PlaneAnimation import PlaneAnimation
from const import fps


class PlaneAnimationFall(PlaneAnimation):
    def __init__(self, plane):
        super().__init__(plane)
        self.velocity = [-5.0, 0.0]

    def animate(self):
        if self.frame == 0:
            self.sprite.current_img = pygame.Surface((4, 4))
            self.sprite.current_img.fill('black')
            self.sprite.move(1280 - self.sprite.current_img.get_size()[0] - 80, 10)
        if self.frame == 5 * fps:
            self.sprite.size = [40, 40]
            self.sprite.x = self.sprite.x - self.sprite.size[0] // 2
            self.sprite.y = self.sprite.y - self.sprite.size[1]
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[2][0], self.sprite.size)

        if self.frame <= fps * 2:
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.velocity[0] += 0.010
            self.velocity[1] += 0.015
        elif fps * 2 < self.frame <= fps * 3:
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.velocity[0] += 0.027
            self.velocity[1] += 0.015
        elif fps * 3 < self.frame <= fps * 5:
            self.sprite.x += self.velocity[0]
            self.sprite.y += self.velocity[1]
            self.velocity[1] += 0.015

        if self.frame == 9 * fps:
            self.is_play = False
            self.is_finish = True
            self.frame = 0
            self.sprite.size = [0, 0]
            self.sprite.current_img = pygame.transform.scale(self.sprite.sprites[2][0], self.sprite.size)
