import pygame, const
from pygame import Surface

from Sprites.Sprite import Sprite


class UIBackgroundSprite(Sprite):
    def __init__(self):
        self.scene = None
        self.image = self._init_image()
        self.image = pygame.transform.scale(self.image, (const.screen_width, const.screen_height))

        super().__init__(0, 0, *self.image.get_size())

    def draw(self, screen: Surface):
        screen.blit(self.image, (0, 0))

    def _init_image(self) -> pygame.image:
        image = pygame.image.load('Scene/scene.png')
        return image
