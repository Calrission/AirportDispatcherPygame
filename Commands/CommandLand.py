from Screens.Game import AircraftController
from Commands.Command import Command
from MultiLineText import MultiLineText
from Terminals.AircraftsTerminal import AircraftsTerminal


class CommandLand(Command):
    @staticmethod
    def get_command_prefix():
        return "land"

    @staticmethod
    def get_description():
        return "Сажает самолёт по указанному ID на указанною полосу"

    @staticmethod
    def get_signature():
        return "land {ID самолёта} {A или B - полоса}"

    @staticmethod
    def get_requirements():
        return [AircraftController, MultiLineText, AircraftsTerminal]

    def execute(self, *args):
        controller: AircraftController = self._get_requirement(AircraftController, args)
        out: MultiLineText = self._get_requirement(MultiLineText, args)
        terminal: AircraftsTerminal = self._get_requirement(AircraftsTerminal, args)
        try:
            id = self._params[0]
            way = self._params[1]
            aircraft = controller.get_aicraft(id)
            controller.landing(aircraft, way)
            terminal.remove(id)
        except Exception:
            out.add_text("Ошибка при выполнении команды")



