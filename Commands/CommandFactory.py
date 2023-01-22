from const import prefix_commands
from Commands.Command import Command


class CommandFactory:

    @staticmethod
    def get_command(text: str) -> Command | None:
        text = text.split(" ")
        prefix = text[0]
        text = " ".join(text[1:])
        if prefix in prefix_commands:
            command = prefix_commands[prefix]()
        else:
            return None
        command.parse_text_command(text)
        return command
