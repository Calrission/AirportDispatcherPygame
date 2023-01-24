import pygame.font


class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option = 0

    def append_option(self, option, callback):
        self._option_surfaces.append(pygame.font.SysFont('arial', 50).render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option = max(0, min(self._current_option + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option]()

    def draw(self, surf, x, y, option_padding):
        for i, option in enumerate(self._option_surfaces):
            rect = option.get_rect()
            rect.topleft = (x, y + i * option_padding)
            if i == self._current_option:
                pygame.draw.rect(surf, (0, 100, 0), rect)
            surf.blit(option, rect)

    def parse_event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                self.switch(-1)
            elif e.key == pygame.K_s:
                self.switch(1)
            elif e.key == pygame.K_SPACE:
                self.select()