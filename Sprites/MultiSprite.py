from Sprites.Sprite import Sprite
from pygame import Surface
import pygame
from const import screen_width, screen_height


class MultiSprite(Sprite):
    def __init__(self, x: int, y: int, images: list, size=[0, 0]):
        super().__init__(x, y)
        self.sprites = []
        for i in images:
            self.sprites.append(pygame.image.load(i))
        self.current_img = self.sprites[0]

        if size == (0, 0):
            self.size = self.current_img.get_size()
        else:
            self.size = size


    def changeSprite(self, img: str):
        self.current_img  = self.sprites[self.sprites.index(img)]
        self.size = self.current_img.get_size()

    def draw(self, screen: Surface):
        screen.blit(self.current_img, (self.x, self.y))
