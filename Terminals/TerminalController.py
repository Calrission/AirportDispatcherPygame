from SmartScreen import SmartScreen
from Terminals.AircraftsTerminal import AircraftsTerminal
from Terminals.CommandInputTerminal import CommandInputTerminal


class TerminalController:
    def __init__(self, smart_screen: SmartScreen, aircontr):
        self.smart_screen = smart_screen

        self.input_terminal = CommandInputTerminal(24, 510, 590, 190)
        self.output_terminal = AircraftsTerminal(665, 510, 590, 190, aircontr)

    def refresh(self):
        self.input_terminal.refresh(self.smart_screen.screen)
        self.output_terminal.refresh(self.smart_screen.screen)

    def tick(self):
        self.input_terminal.tick()

    def parse_event(self, event):
        self.input_terminal.parse_event(event)
