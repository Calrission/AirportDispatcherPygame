from typing import Type


class Command:
    @staticmethod
    def get_command_prefix():
        return "test"

    @staticmethod
    def get_description():
        return "test command"

    @staticmethod
    def get_signature():
        return Command.get_command_prefix()

    def __init__(self):
        self._params = []

    def parse_text_command(self, text: str):
        if len(text) != 0:
            self._params = text.split(" ") if " " in text else [text]

    def execute(self, *args):
        print(f"Hello, I am test command :)\nYour {self._params=}")

    @staticmethod
    def _get_requirement(requirement: Type, objects: tuple):
        for i in objects:
            if i.__class__ == requirement:
                return i
        return None

    @staticmethod
    def get_requirements():
        return []
