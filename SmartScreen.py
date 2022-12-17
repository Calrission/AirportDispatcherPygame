import pygame

from Sprites.Sprite import Sprite


class SmartScreen:
    def __init__(self, screen: pygame.Surface, background_color: pygame.Color):
        self.screen = screen
        self.background_color = background_color
        self._sprites = []

    def add_sprite(self, sprite: Sprite):
        self._sprites.append(sprite)

    def remove_sprite(self, sprite: Sprite):
        self._sprites.remove(sprite)

    def get_sprite(self, index: int):
        return self._sprites[index]

    def refresh(self):
        self.screen.fill(self.background_color)
        for sprite in self._sprites:
            sprite.draw(self.screen)
            sprite.update()
