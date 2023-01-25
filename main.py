import pygame

from AircraftController import AircraftController
from Commands.CommandExecutor import CommandExecutor
from GameClock import GameClock
from Sprites.UIBackgroundSprite import UIBackgroundSprite
from Sprites.UIFrameSprite import UIFrameSprite
from SmartScreen import SmartScreen
from Sprites.TimeSprite import TimeSprite
from Terminals.TerminalController import TerminalController
from const import screen_width, screen_height, fps
from Scenario.Scenario import Scenario
from Sprites.Menu.Menu import Menu

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
    plane1 = controller.add_new_plane(smart_screen, '001')
    plane2 = controller.add_new_plane(smart_screen, '002')
    plane3 = controller.add_new_plane(smart_screen, '003')
    plane4 = controller.add_new_plane(smart_screen, '004')

    smart_screen.add_sprite(frame_sprite)
    smart_screen.add_sprite(clock_sprite)

    controller.landing(plane1, 'A')
    controller.landing(plane2, 'B')
    controller.take_off(plane3, 'A')
    controller.take_off(plane4, 'B')
    controller.fall(plane4)

    scenario = Scenario()
    scenario.add_land('001', 'A', 5 * fps)
    scenario.add_land('002', 'B', 6 * fps)
    scenario.add_land('003', 'A', 7 * fps)
    scenario.add_take_off('004', 'A', 10 * fps)

    menu = Menu()

    menu.append_option('Levels', lambda: print('Открыть уровни'))
    menu.append_option('Exit', lambda: pygame.quit())

    terminalController = TerminalController(smart_screen, controller)
    commandExecutor = CommandExecutor(controller, terminalController.input_terminal.text_view)
    terminalController.input_terminal.command_detect = lambda command: commandExecutor.execute(command)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            terminalController.parse_event(event)
            menu.parse_event(event)

        game_clock.tick()
        clock_sprite.change_time_pos(game_clock.hour, game_clock.minute)
        clock.tick(fps)

        smart_screen.refresh()
        menu.draw(smart_screen.screen, 100, 100, 75)

        terminalController.refresh()
        terminalController.tick_scenario(scenario)
        terminalController.tick()

        pygame.display.flip()

    pygame.quit()
