import pygame
from math import *
from Clock import Clock

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Перетаскивание')
    size = width, height = 201, 201
    center = width // 2
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    running = True
    FPS = 1

    clock = pygame.time.Clock()
    cl = Clock(75, 50)





    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((0, 0, 0))

        pygame.draw.line(screen, (255, 255, 255), (center, center), cl.get_minut_coord(center, center), 1)
        pygame.draw.line(screen, (255, 255, 255), (center, center), cl.get_hour_coord(center, center), 1)
        cl._update()


        clock.tick(FPS)
        pygame.display.flip()

    pygame.quit()