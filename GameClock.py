class GameClock:
    def __init__(self, hour: int = 0, minute: int = 0):
        self.hour = hour
        self.minute = minute

    def get_minute(self):
        return self.minute * 5

    def get_hour(self):
        return self.hour

    def tick(self):
        self.minute += 1
        if self.minute == 12:
            self.minute = 0
            self.hour += 1
            if self.hour == 12:
                self.hour = 0
