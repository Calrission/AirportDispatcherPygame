from Screens.Game import AircraftController
from Commands.Command import Command
from Terminals.AircraftsTerminal import AircraftsTerminal
from Sprites.FlyTransport import StatusFlyTransport
from Terminals.ScrollMultiLineText import ScrollMultiLineText


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
        return [AircraftController, ScrollMultiLineText, AircraftsTerminal]

    def execute(self, *args):
        controller: AircraftController = self._get_requirement(AircraftController, args)
        out: ScrollMultiLineText = self._get_requirement(ScrollMultiLineText, args)
        terminal: AircraftsTerminal = self._get_requirement(AircraftsTerminal, args)
        try:
            id = self._params[0]
            way = self._params[1].upper()
            if way not in ["A", "B"]:
                out.add_text("Только полосы A и B")
                return
            aircraft = controller.get_aicraft(id)
            if aircraft is None:
                out.add_text(f"Самолет с ID={id} не найден")
                return
            if aircraft.status != StatusFlyTransport.FLY:
                out.add_text("Данный самолет уже не находиться в воздухе или больше не может приземлиться")
                return
            if aircraft.animation is None:
                controller.landing(aircraft, way)
                terminal.remove(id)
            else:
                out.add_text("Этот самолет уже невозможно посадить")
        except Exception as e:
            out.add_text("Ошибка при выполнении команды")
            print(e)



