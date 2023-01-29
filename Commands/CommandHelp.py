from Commands.Command import Command
from Terminals.ScrollMultiLineText import ScrollMultiLineText
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
        return [ScrollMultiLineText]

    def execute(self, *args):
        out: ScrollMultiLineText = self._get_requirement(ScrollMultiLineText, args)
        out.add_all_text([f"\"{i.get_signature()}\" - {i.get_description()}" for i in commands])
