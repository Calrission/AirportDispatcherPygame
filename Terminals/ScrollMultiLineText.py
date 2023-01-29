import pygame
from pygame import Surface

from MultiLineText import MultiLineText


class ScrollMultiLineText(MultiLineText):
    def __init__(self, x, y, w, h, color="white", size=24, font=pygame.font.get_default_font(), text="", save_len=-1, save_index_start=None):
        super().__init__(x, y, w, h, color=color, size=size, font=font, text=text, save_len=save_len, save_index_start=save_index_start)

    def _filter_showing_surface(self, surfaces: list[Surface]) -> list[Surface]:
        surfaces = surfaces[::-1]
        sum_h = 0
        filter_surface = []
        for i in surfaces:
            h = i.get_rect().height
            if h + sum_h + self.margin > self.h:
                break
            sum_h += h + self.margin
            filter_surface.append(i)
        return filter_surface[::-1]

    def _generate_surface_all_text(self) -> list[Surface]:
        surfaces = super()._generate_surface_all_text()
        return self._filter_showing_surface(surfaces)