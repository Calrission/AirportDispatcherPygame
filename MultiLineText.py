import math

import pygame.font
from pygame import Surface


class MultiLineText:
    def __init__(self, x, y, w, h, color="white", size=24, font=pygame.font.get_default_font()):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.size = size
        self.color = color
        self.text_lines = []
        self.font = pygame.font.Font(font, self.size)

    def change_text(self, text: str):
        if "\n" in text:
            text_lines = text.split("\n")
        else:
            text_lines = [text]
        self.text_lines = text_lines

    def add_text(self, text: str):
        self.text_lines.append(text)

    def add_last(self, text: str):
        self.text_lines[-1] += text

    def remove_last(self):
        self.text_lines[-1] = self.text_lines[-1][:-1]

    def new_line(self):
        self.text_lines.append("")

    def refresh(self, screen: Surface):
        self.__render_multi_line(screen)

    def __create_text_surface(self, text: str):
        return self.font.render(text, True, self.color)

    def __render_multi_line(self, screen: Surface):
        surfaces = []
        for i in self.text_lines:
            surfaces_line = self.__generate_line_surfaces(i)
            surfaces += surfaces_line
        for i, s in enumerate(surfaces):
            rect = s.get_rect()
            height_text, width_text = rect.height, rect.width
            screen.blit(s, (self.x, self.y + (height_text + 10) * i))

    def __generate_line_surfaces(self, line: str) -> list[Surface]:
        line_surface = self.__create_text_surface(line)
        count_surface = math.ceil(line_surface.get_rect().width / self.w)
        if count_surface <= 1:
            return [line_surface]
        surfaces = []
        sim_w = line_surface.get_rect().width // len(line)
        max_sim_line = self.w // sim_w
        for i in range(count_surface):
            text = line[i * max_sim_line: i * max_sim_line + max_sim_line]
            surfaces.append(self.__create_text_surface(text))
        return surfaces
