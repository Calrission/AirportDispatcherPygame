from Scenario.Scenario import Scenario
from SmartScreen import SmartScreen
from SoundController import SoundController
from Terminals.AircraftsTerminal import AircraftsTerminal
from Terminals.CommandInputTerminal import CommandInputTerminal


class TerminalController:
    def __init__(self, smart_screen: SmartScreen, aircontr, sound: SoundController):
        self.smart_screen = smart_screen

        self.input_terminal = CommandInputTerminal(24, 510, 590, 190, sound)
        self.output_terminal = AircraftsTerminal(665, 510, 590, 190, aircontr)

    def refresh(self):
        self.input_terminal.refresh(self.smart_screen.screen)
        self.output_terminal.refresh(self.smart_screen.screen)

    def tick(self):
        self.input_terminal.tick()

    def tick_scenario(self, scenario: Scenario):
        scenario.time += 1
        if scenario.time % 10 == 0:
            for id, runWay, t, time, elapsedTime, status in scenario.scenario:
                if scenario.time >= time:
                    self.output_terminal.add_aircraft(f'{id} запрашивает {t} {runWay}.', elapsedTime)
                    scenario.scenario.remove((id, runWay, t, time, elapsedTime, status))

    def parse_event(self, event):
        self.input_terminal.parse_event(event)
