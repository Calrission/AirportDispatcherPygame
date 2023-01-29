import sys

import pygame

from Screens.Game import Game
from Screens.Screen import Screen
from const import screen_width, screen_height, fps
from Scenario.Scenario import Scenario
from Screens.Menu import Menu
from Screens.Settings import Settings
from Screens.Levels import Levels


class App:
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load('Music/Main.mp3')
        pygame.mixer.music.play(-1)
        self.s_button = pygame.mixer.Sound('Music/Button.wav')
        pygame.font.init()
        pygame.display.set_caption('Диспетчер')

        self.running = True

        size = screen_width, screen_height
        self.surface = pygame.display.set_mode(size)

        self.clock = pygame.time.Clock()

        self.scenario = Scenario()

        self.menu = Menu(100, 100, 100, self.surface, 'Sprites/Menu/Level_background.png')
        self.levels = Levels(100, 100, 100, self.surface, 'Sprites/Menu/Level_background.png')
        self.settings = Settings(100, 100, 100, self.surface, 'Sprites/Menu/Level_background.png', 'Settings.set')


        self.now_screen: Screen = self.menu

        self.menu.append_option("Отладка: Старт", lambda: self.change_screen(Game(self.surface, self.load_level('Scenario/debagScenario.scen'), self.clock)))
        self.menu.append_option('Уровни', lambda: self.change_screen(self.levels))
        self.menu.append_option('Настройки', lambda: self.change_screen(self.settings))
        self.menu.append_option('О программе', lambda: print('Экран о программе'))
        self.menu.append_option('Выход', lambda: sys.exit())

        self.levels.append_option('Уровень-1', lambda: self.change_screen(Game(self.surface, self.load_level('Scenario/Level-1.scen'), self.clock)))
        self.levels.append_option('Уровень-2', lambda: self.change_screen(Game(self.surface, self.load_level('Scenario/Level-2.scen'), self.clock)))
        self.levels.append_option('Уровень-3', lambda: self.change_screen(Game(self.surface, self.load_level('Scenario/Level-3.scen'), self.clock)))
        self.levels.append_option('Вернуться', lambda: self.change_screen(self.menu))

        self.settings.append_option('Громкость музыки:', lambda: self.change_screen(self.settings))
        self.settings.append_option('Громкость звуков:', lambda: self.change_screen(self.settings))
        self.settings.append_option('Вернуться', lambda: self.change_screen(self.menu))

    def tick(self):
        self.surface.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.s_button.play()
                self.s_button.set_volume(self.settings.soundVolume)
            self.now_screen.parse_event(event)

        self.clock.tick(fps)

        self.now_screen.draw()

        pygame.display.flip()

    def change_screen(self, screen: Screen):
        self.now_screen = screen

    def load_level(self, file: str):
        self.scenario.load(file)
        return self.scenario
