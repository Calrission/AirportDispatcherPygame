import pygame

from Screens.Game import Game
from Screens.Screen import Screen
from const import screen_width, screen_height, fps
from Scenario.Scenario import Scenario
from Screens.Menu import Menu


class App:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Диспетчер')

        self.running = True

        size = screen_width, screen_height
        self.surface = pygame.display.set_mode(size)

        self.clock = pygame.time.Clock()

        self.scenario = Scenario()

        self.menu = Menu(100, 100, 75, self.surface)
        self.levels = Menu(100, 100, 75, self.surface )

        self.now_screen: Screen = self.menu

        self.menu.append_option("Debug: Start", lambda: self.change_screen(Game(self.surface, self.load_level('Scenario/debagScenario.scen'), self.clock)))
        self.menu.append_option('Levels', lambda: self.change_screen(self.levels))
        self.menu.append_option('Exit', lambda: pygame.quit())

        self.levels.append_option('Level-1', lambda: self.change_screen(Game(self.surface, self.load_level('Scenario/Level-1.scen'), self.clock)))
        self.levels.append_option('Level-2', lambda: self.change_screen(Game(self.surface, self.load_level('Scenario/Level-2.scen'), self.clock)))
        self.levels.append_option('Level-3', lambda: self.change_screen(Game(self.surface, self.load_level('Scenario/Level-3.scen'), self.clock)))

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

    def load_level(self, file: str):
        self.scenario.load(file)
        return self.scenario
