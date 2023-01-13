import pygame
from GameClock import GameClock
from Sprites.UIBackgroundSprite import UIBackgroundSprite
from Sprites.UIFrameSprite import UIFrameSprite
from SmartScreen import SmartScreen
from Sprites.TimeSprite import TimeSprite
from const import screen_width, screen_height, fps
from Sprites.Plane import Plane

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

    plane = Plane.get_instance(0, 0)
    smart_screen.add_sprite(plane)
    plane.takeOff('B')

    plane = Plane.get_instance(0, 0)
    smart_screen.add_sprite(plane)
    plane.landing('B')

    smart_screen.add_sprite(frame_sprite)
    smart_screen.add_sprite(clock_sprite)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_clock.tick()
        clock_sprite.change_time_pos(game_clock.hour, game_clock.minute)

        clock.tick(fps)
        smart_screen.refresh()
        pygame.display.flip()

    pygame.quit()
