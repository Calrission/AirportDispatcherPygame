import pygame
from Screens.Menu import Menu

class Settings(Menu):
    def __init__(self, x: int, y: int, padding: int, surface: pygame.Surface, background: str):
        super().__init__(x, y, padding, surface, background)
        self.musicVolume = 1
        self.soundVolume = 1

        self.statMusic = self.font.render(str(int(self.musicVolume * 100) ), True, (0, 0, 0))
        self.statSound = self.font.render(str(int(self.soundVolume * 100)), True, (0, 0, 0))


    def draw(self):
        super().draw()
        rect = self.statMusic.get_rect()
        rect.topleft = (self.x + 700, self.y)
        self.surface.blit(self.statMusic, rect)

        rect = self.statSound.get_rect()
        rect.topleft = (self.x + 700, self.y + self.padding)
        self.surface.blit(self.statSound, rect)


    def parse_event(self, e):
        super().parse_event(e)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a or e.key == pygame.K_LEFT:
                if self._current_option == 0:
                    self.musicVolume -= 0.1
                    self.musicVolume = max(0, self.musicVolume)
                elif self._current_option == 1:
                    self.soundVolume -= 0.1
                    self.soundVolume = max(0, self.soundVolume)

            elif e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                if self._current_option == 0:
                    self.musicVolume += 0.1
                    self.musicVolume = min(1, self.musicVolume)
                elif self._current_option == 1:
                    self.soundVolume += 0.1
                    self.soundVolume = min(1, self.soundVolume)

            pygame.mixer.music.set_volume(self.musicVolume)
            self.statMusic = self.font.render(str(int(self.musicVolume * 100)), True, (0, 0, 0))
            self.statSound = self.font.render(str(int(self.soundVolume * 100)), True, (0, 0, 0))
