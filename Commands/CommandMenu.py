from Commands.Command import Command


class CommandMenu(Command):
    @staticmethod
    def get_command_prefix():
        return "menu"

    @staticmethod
    def get_description():
        return "Выход в меню"

    @staticmethod
    def get_signature():
        return "menu"

    @staticmethod
    def get_requirements():
        return []

    @staticmethod
    def get_dict_requirement():
        return ["finish_game"]

    def execute(self, *args, **kwargs):
        finish_game = kwargs["finish_game"]
        finish_game()

