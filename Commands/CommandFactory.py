from Commands.Command import Command
from Commands.CommandHelp import CommandHelp
from commands import prefix_commands


class CommandFactory:

    @staticmethod
    def get_command(text: str) -> Command | None:
        text = text.split(" ")
        prefix = text[0]
        text = " ".join(text[1:])
        if prefix == CommandHelp.get_command_prefix():
            return CommandHelp()
        if prefix in prefix_commands:
            command = prefix_commands[prefix]()
        else:
            return None
        command.parse_text_command(text)
        return command
