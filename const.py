from Commands.Command import *
from Commands.PrintCommand import PrintCommand

screen_width = 1280
screen_height = 720
screen_center = (screen_width // 2, screen_height // 2)


fps = 30

minute_length = 30
hour_length = 18

commands = [
    Command, PrintCommand
]
prefix_commands = {i.get_command_prefix(): i for i in commands}
