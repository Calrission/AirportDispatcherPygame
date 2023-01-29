from Animation.PlaneAnimationLandA import PlaneAnimationLandA
from Animation.PlaneAnimationLandB import PlaneAnimationLandB
from Animation.PlaneAnimationTakeOffA import PlaneAnimationTakeOffA
from Animation.PlaneAnimationTakeOffB import PlaneAnimationTakeOffB
from Animation.PlaneAnimationFall import PlaneAnimationFall
from Scenario.Scenario import Scenario
from SmartScreen import SmartScreen
from Sprites.FlyTransport import *
from Sprites.Plane import Plane


class AircraftController:
    def __init__(self):
        self.aircrafts = []
        self.way_A = None
        self.way_B = None

        self.count = 0
        self.land_plane_price = 50
        self.take_off_price = 50
        self.fall_price = -50
        self.fail_take_off = -50

    def add_aircraft(self, aircraft: FlyTransport):
        self.aircrafts.append(aircraft)

    def remove_aircraft(self, aircraft: FlyTransport):
        self.aircrafts.remove(aircraft)

    def get_aircraft(self, ID: str) -> FlyTransport:
        for i in self.aircrafts:
            if i.ID == ID:
                return i

    def landing(self, aircraft: FlyTransport, runWay: chr):
        aircraft.show = True
        if aircraft not in self.aircrafts:
            raise ValueError("aircraft not exist in controller")

        if runWay == 'A':
            aircraft.animation = PlaneAnimationLandA(aircraft)
            self.way_A = aircraft
        elif runWay == 'B':
            aircraft.animation = PlaneAnimationLandB(aircraft)
            self.way_B = aircraft

        aircraft.landing()
        self.count += self.land_plane_price

    def take_off(self, aircraft: FlyTransport, runWay: chr):
        aircraft.show = True
        if aircraft not in self.aircrafts:
            raise ValueError("aircraft not exist in controller")

        if runWay == 'A':
            aircraft.animation = PlaneAnimationTakeOffA(aircraft)
        elif runWay == 'B':
            aircraft.animation = PlaneAnimationTakeOffB(aircraft)

        aircraft.takeOff()
        self.count += self.take_off_price

    def fall(self, aircraft: FlyTransport):
        aircraft.show = True
        if aircraft not in self.aircrafts:
            raise ValueError("aircraft not exist in controller")
        aircraft.animation = PlaneAnimationFall(aircraft)
        aircraft.fall()

        self.count += self.fall_price

    def add_new_plane(self, smart_screen: SmartScreen, Plane_ID: str, status: StatusFlyTransport) -> Plane:
        plane = Plane.get_instance(0, 0, Plane_ID, status)
        plane.show = False
        smart_screen.add_sprite(plane)
        self.add_aircraft(plane)
        return plane

    def fill_aircrafts_from_scenario(self, scenario: Scenario, smart_screen: SmartScreen):
        ids = scenario.get_all_init_info_aircrafts()
        for id, status in ids:
            self.add_new_plane(smart_screen, id, status)

    def check_empty_way(self, way: str):
        way = way.upper()
        self.refresh_way_a()
        self.refresh_way_b()
        return (way == 'A' and self.way_A is None) or (way == "B" and self.way_B is None)

    def refresh_way_a(self):
        if self.way_A is not None:
            if isinstance(self.way_A, Plane):
                self.way_A = None if self.way_A.is_already_animate and self.way_A.animation is None else self.way_A

    def refresh_way_b(self):
        if self.way_B is not None:
            if isinstance(self.way_B, Plane):
                self.way_B = None if self.way_B.is_already_animate and self.way_B.animation is None else self.way_B
