import pygame.font
from const import screen_width, screen_height
from Screens.Screen import Screen


class Menu(Screen):
    def __init__(self, x: int, y: int, padding: int, surface: pygame.Surface, background: str):
        super().__init__(x, y, surface)
        self.padding = padding
        self._option_surfaces = []
        self._callbacks = []
        self._current_option = 0
        self.font = pygame.font.Font('Fonts/AmaticSC-Bold.ttf', 76)
        self.background = pygame.transform.scale(pygame.image.load(background), (screen_width, screen_height))

    def append_option(self, option, callback):
        self._option_surfaces.append(self.font.render(option, True, (0, 0, 0)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option = max(0, min(self._current_option + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option]()

    def draw(self):
        self.surface.blit(self.background, (0, 0))
        for i, option in enumerate(self._option_surfaces):
            rect = option.get_rect()
            rect.topleft = (self.x, self.y + i * self.padding)
            if i == self._current_option:
                pygame.draw.rect(self.surface, (0, 200, 0), rect)
            self.surface.blit(option, rect)

    def parse_event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w or e.key == pygame.K_UP:
                self.switch(-1)
            elif e.key == pygame.K_s or e.key == pygame.K_DOWN:
                self.switch(1)
            elif e.key == pygame.K_SPACE or e.key == pygame.K_RETURN:
                self.select()




