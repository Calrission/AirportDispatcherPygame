from TimerFPS import Timer
class GameClock(Timer):
    def __init__(self, hour: int = 0, minute: int = 0, fps: int = 30, requiredTime: float = 1):
        super().__init__(fps=fps, time=requiredTime)
        self.hour = hour
        self.minute = minute
        self.fps = fps
        self.frame_number = 0

    def get_minute(self):
        return self.minute * 5

    def get_hour(self):
        return self.hour

    def tick(self):
        if self.timer_tick():
            self.minute += 1
            if self.minute == 12:
                self.minute = 0
                self.hour += 1
                if self.hour == 12:
                    self.hour = 0
