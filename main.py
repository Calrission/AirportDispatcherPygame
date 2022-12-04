import pygame
from GameClock import GameClock
from SmartScreen import SmartScreen
from Sprites.TimeSprite import TimeSprite
from const import screen_width, screen_height, screen_center, fps

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Диспетчер')

    size = width, height = screen_width, screen_height

    clock = pygame.time.Clock()
    game_clock = GameClock()
    clock_sprite = TimeSprite(*screen_center)

    game_clock1 = GameClock(requiredTime=2)
    clock_sprite1 = TimeSprite(screen_center[0] + 100, screen_center[1])

    smart_screen = SmartScreen(pygame.display.set_mode(size), pygame.Color("black"))
    smart_screen.add_sprite(clock_sprite)
    smart_screen.add_sprite(clock_sprite1)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_clock.tick()
        game_clock1.tick()
        clock_sprite.change_time_pos(game_clock.hour, game_clock.minute)
        clock_sprite1.change_time_pos(game_clock1.hour, game_clock1.minute)

        clock.tick(fps)
        smart_screen.refresh()
        pygame.display.flip()

    pygame.quit()
