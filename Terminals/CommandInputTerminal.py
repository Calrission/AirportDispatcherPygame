from Commands.CommandFactory import CommandFactory
from Terminals.InputTerminal import InputTerminal


class CommandInputTerminal(InputTerminal):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def _enter_user_line(self, text: str):
        command = CommandFactory.get_command(text)
        if command is None:
            self._text_view.add_text("Command not found")
        else:
            self._text_view.add_text("Command detect")
