from Commands.CommandFactory import CommandFactory
from Terminals.InputTerminal import InputTerminal


class CommandInputTerminal(InputTerminal):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.command_detect = lambda command: None

    def _enter_user_line(self, text: str):
        command = CommandFactory.get_command(text)
        if command is None:
            self.text_view.add_text("Command not found")
        else:
            self.command_detect(command)

