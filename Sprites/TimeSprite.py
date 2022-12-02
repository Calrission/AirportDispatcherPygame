import pygame
from pygame import Surface
from math import cos, sin, radians
from Sprites.SingleSprite import SingleSprite
from const import hour_length, minute_length


class TimeSprite(SingleSprite):
    def __init__(self, x: int, y: int, hour: int = 0, minute: int = 0):
        super().__init__(x, y, "clock.png")
        self.hour_length = hour_length
        self.minute_length = minute_length
        self.minute_pos = minute
        self.hour_pos = hour

    def change_time_pos(self, hour_pos: int, minute_pos: int):
        self.minute_pos, self.hour_pos = minute_pos, hour_pos

    def get_minute_angle(self):
        return self.minute_pos * 30

    def get_hour_angle(self):
        return self.hour_pos * 30

    def get_minute_coord(self):
        return (self.minute_length * cos(radians(self.get_minute_angle() - 90)) + self.x,
                self.minute_length * sin(radians(self.get_minute_angle() - 90)) + self.y)

    def get_hour_coord(self):
        return (self.hour_length * cos(radians(self.get_hour_angle() - 90)) + self.x,
                self.hour_length * sin(radians(self.get_hour_angle() - 90)) + self.y)

    def draw(self, screen: Surface):
        super().draw(screen)
        pygame.draw.line(screen, (255, 255, 255), self.coord, self.get_minute_coord(), 1)
        pygame.draw.line(screen, (255, 255, 255), self.coord, self.get_hour_coord(), 1)


