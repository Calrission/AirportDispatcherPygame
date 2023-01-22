import const
from Commands.Command import Command


class CommandFactory:
    commands = {i.get_command_prefix(): i for i in const.commands}

    @staticmethod
    def get_command(text: str) -> Command:
        text = text.split(" ")
        prefix = text[0]
        text = " ".join(text[1:])
        if prefix in CommandFactory.commands:
            command = CommandFactory.commands[prefix]()
        else:
            raise ValueError(f"Command with {prefix=} not found")
        command.parse_text_command(text)
        return command
