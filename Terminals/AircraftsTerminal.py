from pygame import Surface
from MultiLineText import MultiLineText
from const import fps
import sys


class AircraftsTerminal:
    def __init__(self, x, y, w, h):
        self.__text_view = MultiLineText(x, y, w, h, color="green", size=16)
        self.aircrafts = []  # (text, elapsed_time)
        self.frame = 0

    def add_aircraft(self, aircraft: str, time: int):
        self.aircrafts.append([aircraft, time])
        self.pr()

    def pr(self):
        self.__text_view.change_text('')
        for i in self.aircrafts:
            self.__text_view.add_text(f'{i[0]} Осталось {i[1]}с')

    def tick(self):
        if self.frame % fps == 0:
            for i in range(len(self.aircrafts)):
                self.aircrafts[i][1] -= 1
                if self.aircrafts[i][1] < 0:
                    print('LOL')
                    sys.exit(0)
            self.pr()

    def refresh(self, screen: Surface):
        self.__text_view.refresh(screen)
        self.frame += 1
        self.tick()
