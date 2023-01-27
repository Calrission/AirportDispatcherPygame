from pygame import Surface
from MultiLineText import MultiLineText
from const import fps
from AircraftController import AircraftController
import sys


class AircraftsTerminal:
    def __init__(self, x, y, w, h, controller: AircraftController):
        self.__text_view = MultiLineText(x, y, w, h, color="green", size=20, font='Fonts/clacon2.ttf')
        self.aircrafts = []  # (text, elapsed_time)
        self.frame = 0
        self.controller = controller

    def add_aircraft(self, aircraft: str, time: int):
        self.aircrafts.append([aircraft, time])
        self.pr()

    def pr(self):
        self.__text_view.change_text('')
        for i in self.aircrafts:
            self.__text_view.add_text(f'{i[0]} Осталось {i[1]}с')

    def tick(self):
        if self.frame % fps == 0:
            d = []
            for i in range(len(self.aircrafts)):
                self.aircrafts[i][1] -= 1
                if self.aircrafts[i][1] < 0:
                    self.controller.fall(self.controller.get_aicraft(self.aircrafts[i][0].split()[0]))
                    d.append(i)
            for i in d:
                del self.aircrafts[i]
            self.pr()

    def refresh(self, screen: Surface):
        self.__text_view.refresh(screen)
        self.frame += 1
        self.tick()
