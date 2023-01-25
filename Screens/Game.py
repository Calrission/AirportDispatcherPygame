import pygame
from pygame.time import Clock

from AircraftController import AircraftController
from Commands.CommandExecutor import CommandExecutor
from GameClock import GameClock
from Screens.Screen import Screen
from Sprites.UIBackgroundSprite import UIBackgroundSprite
from Sprites.UIFrameSprite import UIFrameSprite
from SmartScreen import SmartScreen
from Sprites.TimeSprite import TimeSprite
from Terminals.TerminalController import TerminalController
from const import screen_width
from Scenario.Scenario import Scenario


class Game(Screen):
    def __init__(self, surface: pygame.Surface, scenario: Scenario, clock: Clock):
        super().__init__(0, 0, surface)
        self.scenario = scenario
        self.clock = clock

        self.game_clock = GameClock()

        self.clock_sprite = TimeSprite(screen_width - 105, 95)
        self.background_sprite = UIBackgroundSprite()
        self.frame_sprite = UIFrameSprite()

        self.smart_screen = SmartScreen(surface, pygame.Color("black"))
        self.smart_screen.add_sprite(self.background_sprite)

        self.controller = AircraftController()
        plane1 = self.controller.add_new_plane(self.smart_screen, '001')
        plane2 = self.controller.add_new_plane(self.smart_screen, '002')
        plane3 = self.controller.add_new_plane(self.smart_screen, '003')
        plane4 = self.controller.add_new_plane(self.smart_screen, '004')

        self.smart_screen.add_sprite(self.frame_sprite)
        self.smart_screen.add_sprite(self.clock_sprite)

        self.controller.landing(plane1, 'A')
        self.controller.landing(plane2, 'B')
        self.controller.take_off(plane3, 'A')
        self.controller.take_off(plane4, 'B')
        self.controller.fall(plane4)

        self.terminalController = TerminalController(self.smart_screen, self.controller)
        self.commandExecutor = CommandExecutor(self.controller, self.terminalController.input_terminal.text_view)
        self.terminalController.input_terminal.command_detect = lambda command: self.commandExecutor.execute(command)

    def draw(self):
        self.game_clock.tick()
        self.clock_sprite.change_time_pos(self.game_clock.hour, self.game_clock.minute)

        self.smart_screen.refresh()

        self.terminalController.refresh()
        self.terminalController.tick_scenario(self.scenario)
        self.terminalController.tick()

    def parse_event(self, event):
        self.terminalController.parse_event(event)
