import pygame
from pygame import Surface

from Sprites.UIBackgroundSprite import UIBackgroundSprite


class UIFrameSprite(UIBackgroundSprite):
    def _init_image(self) -> pygame.image:
        image = pygame.image.load('Scene/Frame.png')
        return image
