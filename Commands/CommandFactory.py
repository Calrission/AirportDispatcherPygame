import const
from Commands.Command import Command


class CommandFactory:
    commands = {i.get_command_prefix(): i for i in const.commands}

    @staticmethod
    def get_command(command: str) -> Command | None:
        if command in CommandFactory.commands:
            return CommandFactory.commands[command]
        return None
