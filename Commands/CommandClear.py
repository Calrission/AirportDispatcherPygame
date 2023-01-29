from Commands.Command import Command
from MultiLineText import MultiLineText


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
        return [MultiLineText]

    def execute(self, *args):
        out: MultiLineText = self._get_requirement(MultiLineText, args)
        out.clear()