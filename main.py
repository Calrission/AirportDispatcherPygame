import pygame

from AircraftController import AircraftController
from GameClock import GameClock
from Sprites.UIBackgroundSprite import UIBackgroundSprite
from Sprites.UIFrameSprite import UIFrameSprite
from SmartScreen import SmartScreen
from Sprites.TimeSprite import TimeSprite
from const import screen_width, screen_height, fps
from Scenario.Scenario import Scenario

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Диспетчер')

    size = width, height = screen_width, screen_height

    clock = pygame.time.Clock()
    game_clock = GameClock()

    clock_sprite = TimeSprite(screen_width - 105, 95)
    background_sprite = UIBackgroundSprite()
    frame_sprite = UIFrameSprite()

    smart_screen = SmartScreen(pygame.display.set_mode(size), pygame.Color("black"))
    smart_screen.add_sprite(background_sprite)

    controller = AircraftController()
    plane1 = controller.add_new_plane(smart_screen)
    plane2 = controller.add_new_plane(smart_screen)
    plane3 = controller.add_new_plane(smart_screen)
    plane4 = controller.add_new_plane(smart_screen)

    controller.landing(plane1, 'A')
    controller.landing(plane2, 'B')
    controller.take_off(plane3, 'A')
    controller.take_off(plane4, 'B')

    smart_screen.add_sprite(frame_sprite)
    smart_screen.add_sprite(clock_sprite)

    scenario = Scenario()
    # scenario.add_Land('A', 10 * fps)
    # scenario.add_Land('B', 20 * fps)
    # scenario.add_Land('A', 15 * fps)
    #
    # scenario.add_takeOff('B', 9 * fps)
    # scenario.add_takeOff('A', 14 * fps)
    # scenario.add_takeOff('A', 16 * fps)

    # scenario.save('test.scen')

    scenario.load('test.scen')

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_clock.tick()
        clock_sprite.change_time_pos(game_clock.hour, game_clock.minute)

        scenario.tick()
        clock.tick(fps)
        smart_screen.refresh()
        pygame.display.flip()

    pygame.quit()
