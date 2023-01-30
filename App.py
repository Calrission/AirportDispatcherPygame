import sys
import os
import pygame

from Screens.Game import Game
from Screens.Screen import Screen
from const import screen_width, screen_height, fps
from Scenario.Scenario import Scenario
from Screens.Menu import Menu
from Screens.Settings import Settings
from Screens.Levels import Levels
from Screens.AboutAs import AboutAs
from Saves.ScoreSaver import ScoreSaver
from SoundController import SoundController


class App:
    def __init__(self):
        lastLevel_path = 'Saves/LastLevel.txt'
        try:
            if os.path.exists(lastLevel_path):
                with open(lastLevel_path, 'rt') as f:
                    self.lastLevel = f.read()
            else:
                with open(lastLevel_path, 'wt') as f:
                    f.write('Scenario/Level-1.scen')
                    self.lastLevel = 'Scenario/Level-1.scen'
        except Exception as ex:
            print('Ошибка загрузки последнего уровня\n', ex)

        pygame.init()
        pygame.mixer.music.load('Music/Main.mp3')
        pygame.mixer.music.play(-1)

        self.sound_Controller = SoundController()
        self.sound_Controller.add_sound('Music/Button.wav')
        self.sound_Controller.add_sound('Music/land.wav')
        self.sound_Controller.add_sound('Music/TakeOff.wav')
        self.sound_Controller.add_sound('Music/Boom.wav')

        pygame.font.init()
        pygame.display.set_caption('Диспетчер')

        self.running = True

        size = screen_width, screen_height
        self.surface = pygame.display.set_mode(size)

        self.clock = pygame.time.Clock()

        self.scenario = Scenario()
        scores = ScoreSaver('Saves/Score.set')

        self.menu = Menu(100, 100, 100, self.surface, 'Sprites/Menu/Level_background.png', self.sound_Controller)
        self.levels = Levels(100, 100, 100, self.surface, 'Sprites/Menu/Level_background.png', scores, self.sound_Controller)
        self.aboutAs = AboutAs(80, screen_height // 2, 100, self.surface, 'Sprites/Menu/Level_background.png', self.sound_Controller)
        self.settings = Settings(100, 100, 100, self.surface, 'Sprites/Menu/Level_background.png', 'Saves/Settings.set', self.sound_Controller)

        self.now_screen: Screen = self.menu

        self.menu.append_option("Старт", lambda: self.change_screen(
            Game(self.surface, self.load_level(self.lastLevel), self.clock, self.finish_game, scores, self.sound_Controller, self.lastLevel)))
        self.menu.append_option('Уровни', lambda: self.change_screen(self.levels))
        self.menu.append_option('Настройки', lambda: self.change_screen(self.settings))
        self.menu.append_option('О программе', lambda: self.change_screen(self.aboutAs))
        self.menu.append_option('Выход', lambda: sys.exit())

        self.levels.append_option('Уровень-1', lambda: self.change_screen(
            Game(self.surface, self.load_level('Scenario/Level-1.scen'), self.clock, self.finish_game, scores, self.sound_Controller, self.lastLevel)))
        self.levels.append_option('Уровень-2', lambda: self.change_screen(
            Game(self.surface, self.load_level('Scenario/Level-2.scen'), self.clock, self.finish_game, scores, self.sound_Controller, self.lastLevel)))
        self.levels.append_option('Уровень-3', lambda: self.change_screen(
            Game(self.surface, self.load_level('Scenario/Level-3.scen'), self.clock, self.finish_game, scores, self.sound_Controller, self.lastLevel)))
        self.levels.append_option('Вернуться', lambda: self.change_screen(self.menu))

        self.settings.append_option('Громкость музыки:', lambda: self.change_screen(self.settings))
        self.settings.append_option('Громкость звуков:', lambda: self.change_screen(self.settings))
        self.settings.append_option('Вернуться', lambda: self.change_screen(self.menu))

        self.aboutAs.append_option('Вернуться', lambda: self.change_screen(self.menu))

    def tick(self):
        self.surface.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.now_screen.parse_event(event)

        self.clock.tick(fps)

        self.now_screen.draw()

        pygame.display.flip()

    def change_screen(self, screen: Screen):
        self.now_screen = screen
        if isinstance(screen, Levels):
            screen.reload()

    def load_level(self, file: str):
        self.scenario.load(file)
        return self.scenario

    def finish_game(self):
        self.change_screen(self.menu)
