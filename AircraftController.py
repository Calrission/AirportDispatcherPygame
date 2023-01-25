from Animation.PlaneAnimationLandA import PlaneAnimationLandA
from Animation.PlaneAnimationLandB import PlaneAnimationLandB
from Animation.PlaneAnimationTakeOffA import PlaneAnimationTakeOffA
from Animation.PlaneAnimationTakeOffB import PlaneAnimationTakeOffB
from Animation.PlaneAnimationFall import PlaneAnimationFall
from SmartScreen import SmartScreen
from Sprites.FlyTransport import FlyTransport
from Sprites.Plane import Plane


class AircraftController:
    def __init__(self):
        self.aircrafts = []

    def add_aircraft(self, aircraft: FlyTransport):
        self.aircrafts.append(aircraft)

    def remove_aircraft(self, aircraft: FlyTransport):
        self.aircrafts.remove(aircraft)

    def get_aicraft(self, ID: str) -> FlyTransport:
        for i in self.aircrafts:
            if i.ID == ID:
                return i

    def landing(self, aircraft: FlyTransport, runWay: chr):
        aircraft.show = True
        if aircraft not in self.aircrafts:
            raise ValueError("aircraft not exist in controller")

        if runWay == 'A':
            aircraft.animation = PlaneAnimationLandA(aircraft)
        elif runWay == 'B':
            aircraft.animation = PlaneAnimationLandB(aircraft)

    def take_off(self, aircraft: FlyTransport, runWay: chr):
        aircraft.show = True
        if aircraft not in self.aircrafts:
            raise ValueError("aircraft not exist in controller")

        if runWay == 'A':
            aircraft.animation = PlaneAnimationTakeOffA(aircraft)
        elif runWay == 'B':
            aircraft.animation = PlaneAnimationTakeOffB(aircraft)

    def fall(self, aircraft: FlyTransport):
        aircraft.show = True
        if aircraft not in self.aircrafts:
            raise ValueError("aircraft not exist in controller")
        aircraft.animation = PlaneAnimationFall(aircraft)

    def add_new_plane(self, smart_screen: SmartScreen, Plane_ID:str) -> Plane:
        plane = Plane.get_instance(0, 0, Plane_ID)
        plane.show = False
        smart_screen.add_sprite(plane)
        self.add_aircraft(plane)
        return plane
