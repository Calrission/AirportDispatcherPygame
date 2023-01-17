from AircraftController import AircraftController

class Scenario():
    def __init__(self):
        super().__init__()
        self.time = 0
        self.scenario = []


    def tick(self):
        self.time += 1
        if self.time % 10 == 0:
            for runWay, time, t in self.scenario:
                if self.time >= time:
                    print(runWay, t, time) #Тут вызывать добавление самолётов в список ожидания
                    self.scenario.remove((runWay, time, t))



    def add_Land(self, runWay: chr, time=0):
        self.scenario.append((runWay, time, 'L'))

    def add_takeOff(self, runWay: chr, time=0):
        self.scenario.append((runWay, time, 'O'))

    def add_weather(self):
        pass



