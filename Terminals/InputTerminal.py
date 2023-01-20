import pygame.event
from pygame import Surface

from MultiLineText import MultiLineText


class InputTerminal:
    def __init__(self, x, y, w, h):
        self.__text_view = MultiLineText(x, y, w, h, color="green", size=16)
        self.active_input = True
        self.rect = pygame.Rect((x, y, w, h))

    def add_command(self, command: str):
        self.__text_view.add_text(command)

    def clear(self):
        self.__text_view.change_text("")

    def refresh(self, screen: Surface):
        self.__text_view.refresh(screen)

    def tick(self):
        for event in pygame.event.get():
            self.parse_event(event)

    def parse_event(self, event):
        if event.type == pygame.KEYDOWN and self.active_input:
            if event.key == pygame.K_RETURN:
                self.__text_view.new_line()
            elif event.key == pygame.K_BACKSPACE:
                self.__text_view.remove_last()
            else:
                sim = event.unicode
                if len(self.__text_view.text_lines) == 0:
                    self.__text_view.add_text(sim)
                else:
                    self.__text_view.add_last(sim)
