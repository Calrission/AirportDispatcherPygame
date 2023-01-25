import pygame


class Screen:
    def __init__(self, x: int, y: int, surface: pygame.Surface):
        self.x, self.y = x, y
        self.surface = surface

    def draw(self):
        pass

    def parse_event(self, event: pygame.event.Event):
        pass
