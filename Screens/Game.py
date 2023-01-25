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

        for id, *args in scenario.scenario:
            self.controller.add_new_plane(self.smart_screen, id)

        self.smart_screen.add_sprite(self.frame_sprite)
        self.smart_screen.add_sprite(self.clock_sprite)

        self.terminalController = TerminalController(self.smart_screen, self.controller)
        self.commandExecutor = CommandExecutor(self.controller,
                                               self.terminalController.input_terminal.text_view,
                                               self.terminalController.output_terminal)
        self.terminalController.input_terminal.command_detect = lambda command: self.commandExecutor.execute(command)

    def draw(self):
        self.game_clock.tick()
        self.clock_sprite.change_time_pos(self.game_clock.hour, self.game_clock.minute)

        self.smart_screen.refresh()

        self.terminalController.refresh()
        self.tick_scenario()
        self.terminalController.tick()

    def tick_scenario(self):
        self.scenario.time += 1
        if self.scenario.time % 10 == 0:
            for id, runWay, t, time in self.scenario.scenario:
                if self.scenario.time >= time:
                    self.terminalController.output_terminal.add_aircraft(f'{id} запрашивает {t.value} {runWay}.', 10)
                    self.scenario.scenario.remove((id, runWay, t, time))

    def parse_event(self, event):
        self.terminalController.parse_event(event)
