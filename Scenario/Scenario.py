import pickle


class Scenario:
    def __init__(self):
        super().__init__()
        self.time = 0
        self.scenario = []  # (id, runWay, type, time, elapsed_time)

    def add_land(self, id: str, runWay: chr, time=0, elapsedTime=10):
        self.scenario.append((id, runWay, 'посадку на полосу', time, elapsedTime))

    def add_take_off(self, id: str, runWay: chr, time=0, elapsedTime=10):
        self.scenario.append((id, runWay, 'взлёт с полосы', time, elapsedTime))

    def add_weather(self):
        pass

    def load(self, file):
        with open(file, 'rb') as f:
            self.scenario = pickle.load(f)

    def save(self, file):
        with open(file, 'wb') as f:
            pickle.dump(self.scenario, f)
