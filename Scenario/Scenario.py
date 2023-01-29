import pickle

from Sprites.FlyTransport import StatusFlyTransport


class Scenario:
    def __init__(self):
        super().__init__()
        self.time = 0
        self.scenario = []  # (id, runWay, type, time, elapsed_time, status)

    def add_land(self, id: str, runWay: chr, time=0, elapsedTime=10):
        self.scenario.append((id, runWay, 'посадку на полосу', time, elapsedTime, StatusFlyTransport.FLY))

    def add_take_off(self, id: str, runWay: chr, time=0, elapsedTime=10):
        self.scenario.append((id, runWay, 'взлёт с полосы', time, elapsedTime, StatusFlyTransport.GROUND))

    def get_all_init_info_aircrafts(self) -> list[tuple[str, StatusFlyTransport]]:
        return [(i[0], i[5]) for i in self.scenario]

    def add_weather(self):
        pass

    def load(self, file):
        self.time = 0
        try:
            with open(file, 'rb') as f:
                self.scenario = pickle.load(f)
        except Exception as ex:
            print(ex)

    def save(self, file):
        try:
            with open(file, 'wb') as f:
                pickle.dump(self.scenario, f)
        except Exception as ex:
            print(ex)
