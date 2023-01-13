from Animation.PlaneAnimationLandA import PlaneAnimationLandA
from Animation.PlaneAnimationLandB import PlaneAnimationLandB
from Animation.PlaneAnimationTakeOffA import PlaneAnimationTakeOffA
from Animation.PlaneAnimationTakeOffB import PlaneAnimationTakeOffB
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

    def landing(self, aircraft: FlyTransport, runWay: chr):
        if aircraft not in self.aircrafts:
            raise ValueError("aircraft not exist in controller")

        if runWay == 'A':
            aircraft.animation = PlaneAnimationLandA(aircraft)
        elif runWay == 'B':
            aircraft.animation = PlaneAnimationLandB(aircraft)

    def take_off(self, aircraft: FlyTransport, runWay: chr):
        if aircraft not in self.aircrafts:
            raise ValueError("aircraft not exist in controller")

        if runWay == 'A':
            aircraft.animation = PlaneAnimationTakeOffA(aircraft)
        elif runWay == 'B':
            aircraft.animation = PlaneAnimationTakeOffB(aircraft)

    def add_new_plane(self, smart_screen: SmartScreen) -> Plane:
        plane = Plane.get_instance(0, 0)
        smart_screen.add_sprite(plane)
        self.add_aircraft(plane)
        return plane
