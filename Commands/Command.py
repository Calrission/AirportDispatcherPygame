class Command:

    @staticmethod
    def get_command_prefix():
        return "Test"

    def __init__(self):
        self.__params = []

    def parse_text_command(self, text: str):
        if len(text) != 0:
            self.__params = text.split(" ") if " " in text else [text]

    def execute(self, **kwargs):
        print(f"Hello, I am test command :)\nYour {self.__params=}")
