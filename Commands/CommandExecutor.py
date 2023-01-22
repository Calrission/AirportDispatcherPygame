from AircraftController import AircraftController
from Commands.Command import Command
from MultiLineText import MultiLineText


class CommandExecutor:
    def __init__(self, aircraft: AircraftController, out: MultiLineText):
        self.aircraft = aircraft
        self.out = out
        self.commands_history = []
        self.__command_fun = {
            Command: lambda command: command.execute()
        }

    def execute(self, command: Command):
        self.__command_fun[command.__class__](command)
