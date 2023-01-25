from Commands.Command import Command
from MultiLineText import MultiLineText
from commands import commands


class CommandHelp(Command):
    @staticmethod
    def get_command_prefix():
        return "help"

    @staticmethod
    def get_signature():
        return "help"

    @staticmethod
    def get_description():
        return "Список команд и их описание"

    @staticmethod
    def get_requirements():
        return [MultiLineText]

    def execute(self, *args):
        out: MultiLineText = self._get_requirement(MultiLineText, args)
        out.add_all_text([f"{i.get_signature()} - {i.get_description()}" for i in commands])
