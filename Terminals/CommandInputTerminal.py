from Commands.CommandFactory import CommandFactory
from SoundController import SoundController
from Terminals.InputTerminal import InputTerminal


class CommandInputTerminal(InputTerminal):
    def __init__(self, x, y, w, h, sound: SoundController):
        super().__init__(x, y, w, h, sound)
        self.command_detect = lambda command: None

    def _enter_user_line(self, text: str):
        command = CommandFactory.get_command(text)
        if command is None:
            self.text_view.add_text("Command not found")
        else:
            self.command_detect(command)

