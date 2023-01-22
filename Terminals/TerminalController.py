from Scenario.Scenario import Scenario
from SmartScreen import SmartScreen
from Terminals.AircraftsTerminal import AircraftsTerminal
from Terminals.CommandInputTerminal import CommandInputTerminal


class TerminalController:
    def __init__(self, smart_screen: SmartScreen):
        self.smart_screen = smart_screen

        self.input_terminal = CommandInputTerminal(24, 510, 590, 190)
        self.output_terminal = AircraftsTerminal(665, 510, 590, 190)

    def refresh(self):
        self.input_terminal.refresh(self.smart_screen.screen)
        self.output_terminal.refresh(self.smart_screen.screen)

    def tick_scenario(self, scenario: Scenario):
        scenario.time += 1
        if scenario.time % 10 == 0:
            for id, runWay, t, time in scenario.scenario:
                if scenario.time >= time:
                    self.output_terminal.add_aircraft(f'{id} запрашивает {t} с полосы {runWay}.', 10)
                    scenario.scenario.remove((id, runWay, t, time))

    def parse_event(self, event):
        self.input_terminal.parse_event(event)
