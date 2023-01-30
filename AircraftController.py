from Animation.FailTakeOffAnimation import FailTakeOffAnimation
from Animation.PlaneAnimationLandA import PlaneAnimationLandA
from Animation.PlaneAnimationLandB import PlaneAnimationLandB
from Animation.PlaneAnimationTakeOffA import PlaneAnimationTakeOffA
from Animation.PlaneAnimationTakeOffB import PlaneAnimationTakeOffB
from Animation.PlaneAnimationFall import PlaneAnimationFall
from Scenario.Scenario import Scenario
from SmartScreen import SmartScreen
from SoundController import SoundController
from Sprites.FlyTransport import *
from Sprites.Plane import Plane
from const import fps


class AircraftController:
    def __init__(self, sound: SoundController):
        self.aircrafts: list[FlyTransport] = []
        self.way_A = None
        self.way_B = None

        self.score = 0
        self.land_plane_price = 50
        self.take_off_price = 50
        self.fall_price = -50
        self.fail_take_off_price = -50

        self.finish_game = None

        self.check_collision: list[tuple[FlyTransport, FlyTransport]] = []
        self._is_boom = False
        self._time_after_booom = fps * 3
        self._time = 0

        self.sound = sound

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
        self.sound.play('Music/land.wav')
        self.score += self.land_plane_price

    def take_off(self, aircraft: FlyTransport, runWay: chr):
        aircraft.show = True
        if aircraft not in self.aircrafts:
            raise ValueError("aircraft not exist in controller")

        if runWay == 'A':
            aircraft.animation = PlaneAnimationTakeOffA(aircraft)
            if self.way_A is not None:
                self.check_collision.append((self.way_A, aircraft))
        elif runWay == 'B':
            aircraft.animation = PlaneAnimationTakeOffB(aircraft)
            if self.way_B is not None:
                self.check_collision.append((self.way_B, aircraft))

        aircraft.takeOff()
        self.sound.play('Music/land.wav')
        self.score += self.take_off_price

    def fall(self, aircraft: FlyTransport):
        aircraft.show = True
        if aircraft not in self.aircrafts:
            raise ValueError("aircraft not exist in controller")
        aircraft.animation = PlaneAnimationFall(aircraft)
        aircraft.fall()

        self.score += self.fall_price

    def fail_take_off(self, aircraft: FlyTransport):
        if aircraft not in self.aircrafts:
            raise ValueError("aircraft not exist in controller")
        aircraft.animation = FailTakeOffAnimation(aircraft)
        aircraft.fail_take_off()

        self.score += self.fail_take_off_price

    def boom(self, first: FlyTransport, second: FlyTransport):
        self._is_boom = True
        first.animation.is_play = False
        second.animation.is_play = False

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
                self.way_A = None if self.way_A.is_finish else self.way_A

    def refresh_way_b(self):
        if self.way_B is not None:
            if isinstance(self.way_B, Plane):
                self.way_B = None if self.way_B.is_finish else self.way_B

    def tick_check_collision(self):
        for i in self.aircrafts:
            if i.is_finish:
                self.remove_aircraft(i)
        for first, second in self.check_collision:
            if first.check_collision(second.get_rect()):
                self.boom(first, second)
        if self._is_boom:
            self._time += 1
        if self._time >= self._time_after_booom:
            self.off_all_sound()
            self.finish_game(self.score)
        if len(self.aircrafts) == 0:
            if self.finish_game is not None:
                self.off_all_sound()
                self.finish_game(self.score)

    def off_all_sound(self):
        for i in self.sound.sounds:
            self.sound.stop(i)
