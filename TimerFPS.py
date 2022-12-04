class Timer:
    def __init__(self, fps, time):
        self.fps = fps
        self.time = time
        self.requiredFrame = fps * time
        self.frame = 0


    def timer_tick(self) -> bool:
        self.frame += 1
        if self.requiredFrame == self.frame:
            self.frame = 0
            return True
        return False
