from Commands.Command import Command
from Terminals.ScrollMultiLineText import ScrollMultiLineText


class CommandClear(Command):
    @staticmethod
    def get_command_prefix():
        return "clear"

    @staticmethod
    def get_description():
        return "Очищает терминал дял ввода"

    @staticmethod
    def get_signature():
        return "clear"

    @staticmethod
    def get_requirements():
        return [ScrollMultiLineText]

    def execute(self, *args):
        out: ScrollMultiLineText = self._get_requirement(ScrollMultiLineText, args)
        out.clear()