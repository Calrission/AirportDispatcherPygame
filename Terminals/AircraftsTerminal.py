from pygame import Surface
from MultiLineText import MultiLineText
from SoundController import SoundController
from Sprites.FlyTransport import StatusFlyTransport
from const import fps
from AircraftController import AircraftController
import sys


class AircraftsTerminal:
    def __init__(self, x, y, w, h, controller: AircraftController):
        self.__text_view = MultiLineText(x, y, w, h, color="green", size=20, font='Fonts/clacon2.ttf')
        self.showing_aircrafts_info = []  # (text, elapsed_time)
        self.frame = 0
        self.controller = controller

    def add_aircraft(self, aircraft: str, time: int):
        self.showing_aircrafts_info.append([aircraft, time])
        self.refresh_text()

    def refresh_text(self):
        self.__text_view.change_text('')
        for i in self.showing_aircrafts_info:
            self.__text_view.add_text(f'{i[0]} Осталось {i[1]}с')

    def remove(self, id):
        self.showing_aircrafts_info.remove([i for i in self.showing_aircrafts_info if id in i[0]][0])

    def tick(self):
        if self.frame % fps == 0:
            deads = []
            for i in range(len(self.showing_aircrafts_info)):
                self.showing_aircrafts_info[i][1] -= 1
                aircraft = self.controller.get_aircraft(self.showing_aircrafts_info[i][0].split()[0])
                if self.showing_aircrafts_info[i][1] < 0 and aircraft.animation is None:
                    if aircraft.status == StatusFlyTransport.FLY:
                        self.controller.fall(aircraft)
                    elif aircraft.status == StatusFlyTransport.GROUND:
                        self.controller.fail_take_off(aircraft)
                    deads.append(i)
            for i in deads:
                del self.showing_aircrafts_info[i]
            self.refresh_text()

    def refresh(self, screen: Surface):
        self.__text_view.refresh(screen)
        self.frame += 1
        self.tick()
