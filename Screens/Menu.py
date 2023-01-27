import pygame.font

from Screens.Screen import Screen


class Menu(Screen):
    def __init__(self, x: int, y: int, padding: int, surface: pygame.Surface):
        super().__init__(x, y, surface)
        self.padding = padding
        self._option_surfaces = []
        self._callbacks = []
        self._current_option = 0
        self.font = pygame.font.SysFont('arial', 50)

    def append_option(self, option, callback):
        self._option_surfaces.append(self.font.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option = max(0, min(self._current_option + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option]()

    def draw(self):
        for i, option in enumerate(self._option_surfaces):
            rect = option.get_rect()
            rect.topleft = (self.x, self.y + i * self.padding)
            if i == self._current_option:
                pygame.draw.rect(self.surface, (0, 100, 0), rect)
            self.surface.blit(option, rect)

    def parse_event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w or e.key == pygame.K_UP:
                self.switch(-1)
            elif e.key == pygame.K_s or e.key == pygame.K_DOWN:
                self.switch(1)
            elif e.key == pygame.K_SPACE or e.key == pygame.K_RETURN:
                self.select()



