class Clock:
    def __init__(self, minut_lenght, hour_lenght):
        self.hour_lenght = hour_lenght
        self.minute_lenght = minut_lenght
        self.hour_pos = 0
        self.minute_pos = 0

    def get_minut(self):
        return self.minute_pos * 5
    def get_hour(self):
        return self.hour_pos

    def get_minut_angle(self):
        return self.minute_pos * 30
    def get_hour_angle(self):
        return self.hour_pos * 30

    def get_minut_coord(self, x, y):
        from math import cos, sin, radians
        return (self.minute_lenght * cos(radians(self.get_minut_angle() - 90)) + x,
                 self.minute_lenght * sin(radians(self.get_minut_angle() - 90)) + y)

    def get_hour_coord(self, x, y):
        from math import cos, sin, radians
        return (self.hour_lenght * cos(radians(self.get_hour_angle() - 90)) + x,
                self.hour_lenght * sin(radians(self.get_hour_angle() - 90)) + y)


    def _update(self):
        self.minute_pos += 1
        if self.minute_pos == 12:
            self.minute_pos = 0
            self.hour_pos += 1
            if self.hour_pos == 12:
                self.hour_pos = 0

