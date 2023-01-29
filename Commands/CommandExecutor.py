from typing import Type
from Commands.Command import Command


class CommandExecutor:
    def __init__(self, *args, **kwargs):
        self.requirements = args
        self.dict_data = kwargs
        self.commands_history = []

    def execute(self, command: Command):
        requirements = self.get_requirements_for_command(command.__class__)
        requirements_dict = self.get_requirements_dict_data_for_command(command.__class__)
        command.execute(*requirements, **requirements_dict)

    def get_requirements_for_command(self, command: Type[Command]):
        return [self.__get_requirement(i) for i in command.get_requirements()]

    def get_requirements_dict_data_for_command(self, command: Type[Command]) -> dict:
        return {i: self.dict_data[i] for i in command.get_dict_requirement()}

    def __get_requirement(self, requirement: Type):
        for i in self.requirements:
            if i.__class__ == requirement:
                return i
        return None
