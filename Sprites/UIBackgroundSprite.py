import pygame
from pygame import Surface

from Sprites.Sprite import Sprite


class UIBackgroundSprite(Sprite):
    def __init__(self):
        super().__init__(0, 0)
        self.scene = None
        self.image = None

    def draw(self, screen: Surface):
        if self.scene is None:
            self._init_scene(screen)
        screen.blit(self.scene, (0, 0))

    def _init_scene(self, screen: Surface):
        self.scene = pygame.Surface(screen.get_size())
        self.image = pygame.image.load('Scene/scene.png')
        self.image = pygame.transform.scale(self.image, (screen.get_size()))
        self.scene.blit(self.image, (0, 0))