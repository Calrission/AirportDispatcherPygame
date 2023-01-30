from Animation.PlaneAnimation import PlaneAnimation


class FailTakeOffAnimation(PlaneAnimation):
    def __init__(self, plane):
        super().__init__(plane)
        self.velocity = [-5.0, 0.0]
        self.is_play = False
        self.is_finish = True

