import pygame
from Screens.Menu import Menu
from Saves.ScoreSaver import ScoreSaver


class Levels(Menu):
    def __init__(self, x: int, y: int, padding: int, surface: pygame.Surface, background: str, scores: ScoreSaver):
        super().__init__(x, y, padding, surface, background)
        self.scores = []

        for i in scores.data.values():
            self.scores.append(self.font.render(str(i), True, (0, 0, 0)))

    def draw(self):
        self.surface.blit(self.background, (0, 0))
        for i, option in enumerate(self._option_surfaces):
            rect = option.get_rect()
            rect.topleft = (self.x, self.y + i * self.padding)
            if i == self._current_option:
                pygame.draw.rect(self.surface, (0, 200, 0), rect)
            self.surface.blit(option, rect)

        for i, item in enumerate(self.scores):
            rect = item.get_rect()
            rect.topleft = (self.x + 400, self.y + i * self.padding)
            self.surface.blit(item, rect)
