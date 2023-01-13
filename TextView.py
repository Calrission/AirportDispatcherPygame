import pygame.font
from pygame import Surface


class TextView:
    def __init__(self, x, y, color=(255, 255, 255), size=24):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.text = ""
        self.font = pygame.font.Font(pygame.font.get_default_font(), self.size)

    def change_text(self, text: str):
        self.text = text

    def add_text(self, text: str, sep=""):
        self.text += f"{sep}{text}"

    def refresh(self, screen: Surface):
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))
