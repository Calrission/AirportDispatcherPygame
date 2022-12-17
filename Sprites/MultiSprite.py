from Sprites.Sprite import Sprite
from pygame import Surface
import pygame
from const import screen_width, screen_height


class MultiSprite(Sprite):
    def __init__(self, x: int, y: int, images: list):
        super().__init__(x, y)
        self.sprites = []
        for i in images:
            self.sprites.append(pygame.image.load(i))
        self.current_img = self.sprites[0]

    def changeSprite(self, img: str):
        self.current_img  = self.sprites[self.sprites.index(img)]

    def draw(self, screen: Surface):
        screen.blit(self.current_img, (self.x, self.y))
