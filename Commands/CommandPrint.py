from Commands.Command import Command
from MultiLineText import MultiLineText


class CommandPrint(Command):

    @staticmethod
    def get_command_prefix():
        return "print"

    @staticmethod
    def get_description():
        return "Выводит введённые параметры"

    @staticmethod
    def get_signature():
        return "print [inf params]"

    @staticmethod
    def get_requirements():
        return [MultiLineText]

    def execute(self, *args):
        out: MultiLineText = self._get_requirement(MultiLineText, args)
        out.add_text(" ".join(self._params))
