import pygame
from Screens.Menu import Menu


class Levels(Menu):
    def __init__(self, x: int, y: int, padding: int, surface: pygame.Surface, background: str):
        super().__init__(x, y, padding, surface, background)

