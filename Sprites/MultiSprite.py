from Sprites.Sprite import Sprite
from pygame import Surface
import pygame


class MultiSprite(Sprite):
    def __init__(self, x: int, y: int, images: list, size=[0, 0]):
        self.sprites = []
        for i in images:
            a = []
            for j in i:
                a.append(pygame.image.load(j))
            self.sprites.append(a)
        self.current_img = self.sprites[0][0]

        if size == (0, 0):
            self.size = self.current_img.get_size()
        else:
            self.size = size

        super().__init__(x, y, *self.size)

    def draw(self, screen: Surface):
        screen.blit(self.current_img, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, *self.current_img.get_size())


