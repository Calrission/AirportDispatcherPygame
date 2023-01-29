from Screens.Game import AircraftController
from Commands.Command import Command
from MultiLineText import MultiLineText
from Terminals.AircraftsTerminal import AircraftsTerminal
from Sprites.FlyTransport import StatusFlyTransport


class CommandTakeOff(Command):
    @staticmethod
    def get_command_prefix():
        return "takeoff"

    @staticmethod
    def get_description():
        return "Отправляет самолёт, по указанному ID и полосе, на взлет"

    @staticmethod
    def get_signature():
        return "takeoff {ID самолёта} {A или B - полоса}"

    @staticmethod
    def get_requirements():
        return [AircraftController, MultiLineText, AircraftsTerminal]

    def execute(self, *args):
        controller: AircraftController = self._get_requirement(AircraftController, args)
        out: MultiLineText = self._get_requirement(MultiLineText, args)
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
            if aircraft.status != StatusFlyTransport.GROUND:
                out.add_text("Данный самолет уже не находиться на земле или больше не может взлететь")
                return
            if aircraft.animation is None:
                controller.take_off(aircraft, way)
                terminal.remove(id)
            else:
                out.add_text("Этот самолет уже невозможно отправить на взлет")
        except Exception as e:
            out.add_text("Ошибка при выполнении команды")
            print(e)