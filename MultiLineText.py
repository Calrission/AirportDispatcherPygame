import pygame.font
from pygame import Surface


class MultiLineText:
    def __init__(self, x, y, w, h, color="white", size=24, max_lines=None, font=pygame.font.get_default_font()):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.size = size
        self.color = color
        self.text_lines = []
        self.font = pygame.font.Font(font, self.size)
        self.max_lines = max_lines

    def change_text(self, text: str):
        self.text_lines = [text]

    def add_text(self, text: str):
        self.text_lines.append(text)

    def add_last(self, text: str):
        self.text_lines[-1] += text

    def remove_last(self):
        self.text_lines[-1] = self.text_lines[-1][:-1]

    def refresh(self, screen: Surface):
        self.__render_multi_line(screen)

    def __create_text_surface(self, text: str):
        return self.font.render(text, True, self.color)

    def __render_multi_line(self, screen: Surface):
        for i, l in enumerate(self.text_lines):
            surfaces = self.__generate_line_surfaces(l)
            for s in surfaces:
                rect = s.get_rect()
                height_text, width_text = rect.height, rect.width
                screen.blit(s, (self.x, self.y + (height_text + 10) * i))

    def __generate_line_surfaces(self, line: str) -> list[Surface]:
        line_surface = self.__create_text_surface(line)
        return [line_surface]