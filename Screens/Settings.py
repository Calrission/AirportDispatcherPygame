import pygame
from Screens.Menu import Menu
from SoundController import SoundController
import pickle

class Settings(Menu):
    def __init__(self, x: int, y: int, padding: int, surface: pygame.Surface, background: str, save_file: str, sound_Controller: SoundController):
        super().__init__(x, y, padding, surface, background, sound_Controller)
        self.musicVolume = 1
        self.soundVolume = 1
        self.save_file = save_file

        self.load(self.save_file)

        pygame.mixer.music.set_volume(self.musicVolume)
        self.sound_Controller.set_volume(self.soundVolume, 'Music/Button.wav')
        self.sound_Controller.set_volume(self.soundVolume, 'Music/land.wav')
        self.sound_Controller.set_volume(self.soundVolume, 'Music/TakeOff.wav')
        self.sound_Controller.set_volume(self.soundVolume, 'Music/Boom.wav')

        self.statMusic = self.font.render(str(int(self.musicVolume * 100)), True, (0, 0, 0))
        self.statSound = self.font.render(str(int(self.soundVolume * 100)), True, (0, 0, 0))


    def load(self, file):
        try:
            with open(file, 'rb') as f:
                self.musicVolume, self.soundVolume = pickle.load(f)
        except Exception as ex:
            print(ex)

    def save(self, file):
        try:
            with open(file, 'wb') as f:
                pickle.dump([self.musicVolume, self.soundVolume], f)
        except Exception as ex:
            print(ex)



    def draw(self):
        super().draw()
        rect = self.statMusic.get_rect()
        rect.topleft = (self.x + 700, self.y)
        self.surface.blit(self.statMusic, rect)

        rect = self.statSound.get_rect()
        rect.topleft = (self.x + 700, self.y + self.padding)
        self.surface.blit(self.statSound, rect)

    def select(self):
        super().select()
        if self._current_option == len(self._callbacks) - 1:
            self.save(self.save_file)


    def parse_event(self, e):
        super().parse_event(e)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a or e.key == pygame.K_LEFT:
                self.sound_Controller.play('Music/Button.wav')
                if self._current_option == 0:
                    self.musicVolume -= 0.1
                    self.musicVolume = max(0, self.musicVolume)
                elif self._current_option == 1:
                    self.soundVolume -= 0.1
                    self.soundVolume = max(0, self.soundVolume)

            elif e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                self.sound_Controller.play('Music/Button.wav')
                if self._current_option == 0:
                    self.musicVolume += 0.1
                    self.musicVolume = min(1, self.musicVolume)
                elif self._current_option == 1:
                    self.soundVolume += 0.1
                    self.soundVolume = min(1, self.soundVolume)

            pygame.mixer.music.set_volume(self.musicVolume)
            self.sound_Controller.set_volume(self.soundVolume, 'Music/Button.wav')
            self.sound_Controller.set_volume(self.soundVolume, 'Music/land.wav')
            self.sound_Controller.set_volume(self.soundVolume, 'Music/TakeOff.wav')
            self.sound_Controller.set_volume(self.soundVolume, 'Music/Boom.wav')

            self.statMusic = self.font.render(str(int(self.musicVolume * 100)), True, (0, 0, 0))
            self.statSound = self.font.render(str(int(self.soundVolume * 100)), True, (0, 0, 0))
