import pygame.event
from pygame import Surface

from MultiLineText import MultiLineText


class InputTerminal:
    def __init__(self, x, y, w, h):
        self.text_view = MultiLineText(x, y, w, h, color="green", size=16)
        self.active_input = True
        self.rect = pygame.Rect((x, y, w, h))

    def clear(self):
        self.text_view.change_text("")

    def refresh(self, screen: Surface):
        self.text_view.refresh(screen)

    def tick(self):
        for event in pygame.event.get():
            self.parse_event(event)

    def parse_event(self, event):
        if event.type == pygame.KEYDOWN and self.active_input:
            if event.key == pygame.K_RETURN:
                if len(self.text_view.text_lines) != 0:
                    self._enter_user_line(self.text_view.get_last())
                self.text_view.new_line()
            elif event.key == pygame.K_BACKSPACE:
                self.text_view.remove_last()
            else:
                sim = event.unicode
                if len(self.text_view.text_lines) == 0:
                    self.text_view.add_text(sim)
                else:
                    self.text_view.add_last(sim)

    def _enter_user_line(self, text: str):
        pass
