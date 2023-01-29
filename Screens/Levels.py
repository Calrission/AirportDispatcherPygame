import pygame
from Screens.Menu import Menu


class Levels(Menu):
    def __init__(self, x: int, y: int, padding: int, surface: pygame.Surface, background: str):
        super().__init__(x, y, padding, surface, background)

    def parse_event(self, e):
        super().parse_event(e)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_BACKSPACE:
                self._callbacks[-1]()
