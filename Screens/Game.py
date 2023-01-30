import pygame
from pygame.time import Clock
from AircraftController import AircraftController
from Commands.CommandExecutor import CommandExecutor
from GameClock import GameClock
from Saves.ScoreSaver import ScoreSaver
from Screens.Screen import Screen
from Sprites.UIBackgroundSprite import UIBackgroundSprite
from Sprites.UIFrameSprite import UIFrameSprite
from SmartScreen import SmartScreen
from Sprites.TimeSprite import TimeSprite
from Terminals.TerminalController import TerminalController
from const import screen_width
from Scenario.Scenario import Scenario


class Game(Screen):
    def __init__(self, surface: pygame.Surface, scenario: Scenario, clock: Clock, finish_event, score: ScoreSaver):
        super().__init__(0, 0, surface, finish_event)
        self.scenario = scenario
        self.clock = clock
        self.score_saver = score

        self.game_clock = GameClock()

        self.clock_sprite = TimeSprite(screen_width - 105, 95)
        self.background_sprite = UIBackgroundSprite()
        self.frame_sprite = UIFrameSprite()

        self.smart_screen = SmartScreen(surface, pygame.Color("black"))

        self.controller = AircraftController()
        self.controller.finish_game = self.finish_game
        self.smart_screen.add_sprite(self.background_sprite)

        self.controller.fill_aircrafts_from_scenario(self.scenario, self.smart_screen)

        self.smart_screen.add_sprite(self.frame_sprite)
        self.smart_screen.add_sprite(self.clock_sprite)

        self.terminalController = TerminalController(self.smart_screen, self.controller)
        self.commandExecutor = CommandExecutor(self.controller,
                                               self.terminalController.input_terminal.text_view,
                                               self.terminalController.output_terminal, finish_game=finish_event)
        self.terminalController.input_terminal.command_detect = lambda command: self.commandExecutor.execute(command)

    def draw(self):
        self.game_clock.tick()
        self.clock_sprite.change_time_pos(self.game_clock.hour, self.game_clock.minute)

        self.smart_screen.refresh()

        self.terminalController.refresh()
        self.terminalController.tick_scenario(self.scenario)
        self.terminalController.tick()

        self.controller.tick_check_collision()

    def parse_event(self, event):
        self.terminalController.parse_event(event)

    def finish_game(self, score: int):
        self.score_saver.save(self.scenario.name, str(score))
        self.finish_event()
