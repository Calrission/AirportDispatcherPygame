import pygame


class Screen:
    def __init__(self, x: int, y: int, surface: pygame.Surface, finish_event=None):
        self.x, self.y = x, y
        self.surface = surface
        self.finish_event = finish_event

    def draw(self):
        pass

    def parse_event(self, event: pygame.event.Event):
        pass

    def finish(self):
        if self.finish_event is not None:
            self.finish_event()
