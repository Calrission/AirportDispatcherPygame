import pygame


class SoundController:
    def __init__(self):
        self.sounds = {}

    def add_sound(self, file):
        self.sounds[file] = (pygame.mixer.Sound(file))

    def play(self, file='None', ID=-999):
        if file == 'None' and ID != -999:
            self.sounds.values()[ID].play()
        elif file != 'None' and ID == -999:
            self.sounds[file].play()
        else:
            print('Ошибка воспроизведения', file, ID)

    def set_volume(self, volume: float, file='None', ID=-999):
        if file == 'None' and ID != -999:
            self.sounds.values()[ID].set_volume(volume)
        elif file != 'None' and ID == -999:
            self.sounds[file].set_volume(volume)
        else:
            print('Ошибка установки звука', file, ID, volume)

    def stop(self, file='None', ID=-999):
        if file == 'None' and ID != -999:
            self.sounds.values()[ID].stop()
        elif file != 'None' and ID == -999:
            self.sounds[file].stop()
        else:
            print('Ошибка остановки', file, ID)
