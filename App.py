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
        surface = pygame.display.set_mode(size)

        self.clock = pygame.time.Clock()

        scenario = Scenario()
        scenario.add_land('001', 'A', 5 * fps)
        scenario.add_land('002', 'B', 6 * fps)
        scenario.add_land('003', 'A', 7 * fps)
        scenario.add_take_off('004', 'A', 10 * fps)

        self.menu = Menu(100, 100, 75, surface)
        self.game = Game(surface, scenario, self.clock)

        self.now_screen: Screen = self.menu

        self.menu.append_option("Debug: Start", lambda: self.change_screen(self.game))
        self.menu.append_option('Levels', lambda: print('Открыть уровни'))
        self.menu.append_option('Exit', lambda: pygame.quit())

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.now_screen.parse_event(event)

        self.clock.tick(fps)
        self.menu.draw()

        self.now_screen.draw()

        pygame.display.flip()

    def change_screen(self, screen: Screen):
        self.now_screen = screen