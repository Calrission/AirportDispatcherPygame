import pygame

from AircraftController import AircraftController
from GameClock import GameClock
from Sprites.UIBackgroundSprite import UIBackgroundSprite
from Sprites.UIFrameSprite import UIFrameSprite
from SmartScreen import SmartScreen
from Sprites.TimeSprite import TimeSprite
from TerminalView import TerminalView
from const import screen_width, screen_height, fps

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

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

    smart_screen.add_sprite(frame_sprite)
    smart_screen.add_sprite(clock_sprite)

    controller.landing(plane1, 'A')
    controller.landing(plane2, 'B')
    controller.take_off(plane3, 'A')
    controller.take_off(plane4, 'B')

    terminal = TerminalView(24, 510, 650, 213)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            terminal.parse_event(event)

        game_clock.tick()
        clock_sprite.change_time_pos(game_clock.hour, game_clock.minute)

        clock.tick(fps)
        smart_screen.refresh()
        terminal.refresh(smart_screen.screen)
        pygame.display.flip()

    pygame.quit()
